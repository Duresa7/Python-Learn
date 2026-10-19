# 9. Logical Operators

## Booleans

- Boolean values are `True` and `False`
- Type name: `bool`
- Always capitalized: `True`, not `true`

## The Operators

| Operator | Meaning                                |
|----------|----------------------------------------|
| `and`    | Both conditions must be `True`         |
| `or`     | At least one condition must be `True`  |
| `not`    | Reverses the value (`True` ↔ `False`)  |

## Truth Tables

**`and`**: the only way to get `True` is when both sides are `True`.

| Left    | Right   | `left and right` |
|---------|---------|------------------|
| `True`  | `True`  | `True`           |
| `True`  | `False` | `False`          |
| `False` | `True`  | `False`          |
| `False` | `False` | `False`          |

**`or`**: the only way to get `False` is when both sides are `False`.

| Left    | Right   | `left or right` |
|---------|---------|-----------------|
| `True`  | `True`  | `True`          |
| `True`  | `False` | `True`          |
| `False` | `True`  | `True`          |
| `False` | `False` | `False`         |

## Python Syntax

```python
print(True and True)
# Prints True

print(True or False)
# Prints True

print(not True)
# Prints False

print(not False)
# Prints True
```

*Wrap each expression in `print( )` to see its result. Don't write `False or False == False`: `==` is checked before `and`/`or`, so Python reads it as `False or (False == False)`, which is `True`.*

## Nesting and Order

- Use parentheses `( )` to group conditions, the same way as in math
- Without parentheses, Python checks `not` first, then `and`, then `or`

```python
print((True or False) and False)
# Prints False

print(True or False and False)
# Prints True (and runs first: False and False is False, then True or False is True)
```
