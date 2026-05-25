# DataDeck — Design Patterns Reference

This project practices object-oriented design in Python 3.10+, with strong typing and clean separation of responsibilities.

## What this project teaches

- Abstract classes
- Polymorphism
- Abstract Factory pattern
- Strategy pattern
- Composition through capabilities
- Typed client code
- Clear runtime validation and exception handling

## General constraints

- Python 3.10 or later
- Full type annotations expected
- Follow flake8 style
- Use only standard library modules
- Avoid `eval()` and `exec()`
- Handle invalid combinations with explicit exceptions
- Each exercise package must include an `__init__.py`

---

# Exercise 0 — Creature Factory

## Goal

Build a basic creature system using the **Abstract Factory** pattern.

The point is to create related objects without exposing construction details to client code.

## Core idea

A creature belongs to a family and has:
- a name
- a type description
- an `attack()` method
- a `describe()` method shared by all creatures

## Required structure

### Abstract base class
`Creature`
- stores `name` and `creature_type`
- defines abstract `attack()`
- defines concrete `describe()`

### Concrete creatures
- `Flameling`
- `Pyrodon`
- `Aquabub`
- `Torragon`

### Abstract factory
`CreatureFactory`
- defines:
  - `create_base()`
  - `create_evolved()`

### Concrete factories
- `FlameFactory`
  - base: `Flameling`
  - evolved: `Pyrodon`
- `AquaFactory`
  - base: `Aquabub`
  - evolved: `Torragon`

## What the client script tests

`battle.py`:
- creates factories
- uses one generic function that accepts a factory and tests both creatures
- uses another function that takes two factories and makes base creatures fight

## Main lesson

The client code should depend on factories, not on concrete creature classes.

---

# Exercise 1 — Capabilities

## Goal

Add reusable capabilities that are not tied to the creature hierarchy.

This exercise introduces **multiple inheritance** and **composition of behavior through abstract capabilities**.

## Core idea

A capability is separate from `Creature`.  
This keeps behaviors reusable for future entities.

## Required capability abstractions

### `HealCapability`
- abstract `heal()` method

### `TransformCapability`
- abstract `transform()` method
- abstract `revert()` method
- has persistent state that affects `attack()`

## New creature families

### Healing family
- `Sproutling`
- `Bloomelle`

These inherit from both:
- `Creature`
- `HealCapability`

Factory:
- `HealingCreatureFactory`

### Transforming family
- `Shiftling`
- `Morphagon`

These inherit from both:
- `Creature`
- `TransformCapability`

Factory:
- `TransformCreatureFactory`

## What the client script tests

`capacitor.py`:
- creates a healing factory
- tests base and evolved creatures:
  - `describe()`
  - `attack()`
  - `heal()`
- creates a transforming factory
- tests base and evolved creatures:
  - `describe()`
  - `attack()`
  - `transform()`
  - `attack()` again
  - `revert()`

## Main lesson

A creature can gain extra behavior without changing the base creature abstraction.

The transform family also demonstrates stateful behavior:
- `transform()` changes the attack output
- `revert()` restores normal behavior

---

# Exercise 2 — Abstract Strategy

## Goal

Make battle logic flexible by separating combat behavior from the creatures themselves.

This exercise introduces the **Strategy** pattern.

## Core idea

The same creature can act differently depending on the battle strategy assigned to it.

## Required abstractions

### `BattleStrategy`
Defines:
- `is_valid(creature) -> bool`
- `act(creature)`

## Concrete strategies

### `NormalStrategy`
- valid for any creature
- only calls `attack()`

### `AggressiveStrategy`
- valid only for creatures with transform capability
- calls:
  - `transform()`
  - `attack()`
  - `revert()`

### `DefensiveStrategy`
- valid only for creatures with healing capability
- calls:
  - `attack()`
  - `heal()`

## Error handling

If a creature is not compatible with a strategy:
- `is_valid()` returns `False`
- `act()` raises a dedicated exception with a clear message

## What the client script tests

`tournament.py`:
- creates factories from `ex0` and `ex1`
- creates the three strategies
- defines one battle function that accepts a list of opponents

Each opponent is a tuple:
- `(CreatureFactory, BattleStrategy)`

The tournament logic:
- creates creatures from the provided factories
- uses each opponent’s strategy
- runs every opponent against every other opponent once
- stops cleanly on invalid strategy-creature combinations

## Main lesson

Battle behavior should not be hardcoded into the tournament loop.

The tournament should orchestrate objects, not contain creature-specific logic.

---

# Design pattern summary

## Abstract Factory
Used in `ex0` and reused in later exercises.

Purpose:
- create related objects without binding the client to concrete classes

## Multiple inheritance with capabilities
Used in `ex1`.

Purpose:
- add optional behaviors without forcing them into the base creature class

## Strategy
Used in `ex2`.

Purpose:
- swap battle behavior at runtime without changing the creatures or the tournament engine

---

# Code organization reminders

## Packages
- `ex0/`
- `ex1/`
- `ex2/`

Each package must contain `__init__.py`.

## Root scripts
- `battle.py`
- `capacitor.py`
- `tournament.py`

These scripts are client-side tests and demonstrations of the architecture.

---

# Implementation notes

## Typing
Every public function and method should have explicit type annotations.

## Client code
The scripts should:
- accept abstract types where possible
- avoid direct dependency on concrete implementations
- keep battle logic generic

## Exceptions
Invalid strategy usage should never crash the program silently.
Use explicit exceptions with readable messages.

## Suggested mental model

- `Creature` defines what every creature can do
- factories decide which creatures to build
- capabilities add optional special behavior
- strategies decide how a creature behaves in battle
- the tournament only coordinates the fight

---

# One-line memory aid

Factory creates the creature, capability adds the extra power, strategy decides how it fights.

---

# Typing Notes — TypeGuard, TypeIs, and Intersection Types

This project uses runtime checks plus static typing to make strategy selection safe and explicit.

The strategies in `ex2/strategies.py` illustrate three typing ideas:

- `Protocol`
- `TypeGuard`
- `TypeIs`
- intersection-like typing through protocol composition

---

# Why normal inheritance is not enough

A strategy does not care about the exact concrete class.

It only cares that the object supports the required behavior.

Example:
- aggressive strategy needs:
  - `transform()`
  - `attack()`
  - `revert()`

The concrete class is secondary.

This is why structural typing is useful.

---

# Protocols

Protocols describe the shape of an object.

Example:

```python
class CreatureLike(Protocol):
    def attack(self) -> str: ...
    def describe(self) -> str: ...
```

Any object implementing those methods is compatible.

No explicit inheritance is required.

This is structural typing:
- if it has the required methods, it fits

---

# Capability composition

Protocols can inherit from other protocols.

Example:

```python
class HealCreatureLike(CreatureLike, Protocol):
    def heal(self) -> str: ...
```

This behaves like an intersection of requirements:

- `CreatureLike`
- and `heal()`

So the object must support:
- `attack()`
- `describe()`
- `heal()`

The same idea applies to transforming creatures:

```python
class TransCreatureLike(CreatureLike, Protocol):
    def transform(self) -> str: ...
    def revert(self) -> str: ...
```

Python does not provide a general built-in `A & B` syntax for all types. Protocol inheritance is the idiomatic way to express that an object must satisfy multiple method sets. The typing docs also describe `TypeIs` as combining previously known information with the narrowed type, which is technically an intersection type. :contentReference[oaicite:0]{index=0}

---

# TypeGuard

`TypeGuard[T]` tells the type checker:

> if this function returns `True`, treat the checked value as `T`

Example:

```python
def is_valid(self, monster: object) -> TypeGuard[Creature]:
    return isinstance(monster, Creature)
```

After:

```python
if self.is_valid(monster):
```

the checker understands that `monster` is a `Creature`.

This is why `monster.attack()` becomes valid inside the guarded block.

`TypeGuard` was introduced so user-defined runtime checks can drive static narrowing. Its semantics are one-way: on `True`, the value is narrowed to the target type; on `False`, the checker does not narrow the value further. :contentReference[oaicite:1]{index=1}

---

# TypeIs

`TypeIs[T]` is the newer alternative.

In Python 3.13, `TypeIs` is available in the standard typing module and is described as a more intuitive alternative to `TypeGuard`. :contentReference[oaicite:2]{index=2}

It has two important differences:

## 1. It narrows both branches

- `True` branch: the value is narrowed to the matching type
- `False` branch: the value is narrowed by excluding that type

## 2. It requires compatibility with the input type

`TypeIs` requires the narrowed type to be a subtype of the input type, while `TypeGuard` does not. This restriction is what gives `TypeIs` its stronger and more predictable narrowing behavior. :contentReference[oaicite:3]{index=3}

---

# Tradeoff: TypeGuard vs TypeIs

Use `TypeGuard` when:
- you need maximum flexibility
- the narrowed type is not a strict subtype of the input type
- you are on Python versions before 3.13

Use `TypeIs` when:
- you want better narrowing behavior
- you want the `else` branch narrowed too
- your predicate is compatible with subtype rules
- you are on Python 3.13+

For this project:
- `TypeGuard` is the conservative and broadly compatible choice
- `TypeIs` is the cleaner choice if your type checker and Python version support it

---

# Example from `AggressiveStrategy`

```python
def is_valid(self, monster: object) -> TypeGuard[TransCreatureLike]:
    return isinstance(monster, Creature) and isinstance(monster, TransformCapability)
```

This means:
- the object must be a `Creature`
- the object must also expose the transform capability

After the check succeeds, the checker lets the code use:

```python
monster.transform()
monster.attack()
monster.revert()
```

---

# Why `object` is the input type

Strategies accept:

```python
monster: object
```

instead of a concrete creature type.

That forces explicit validation and makes the strategy generic.

The flow is:

- accept anything
- validate at runtime
- narrow for the type checker
- run the capability-specific behavior

---

# Summary

- `Protocol` describes required behavior
- protocol inheritance expresses intersection-like capability sets
- `TypeGuard` narrows only the `True` branch
- `TypeIs` narrows both branches and is stricter about compatibility
- `TypeIs` is available in Python 3.13
- for capability-based strategies, `TypeGuard` is safe and `TypeIs` is more precise when available