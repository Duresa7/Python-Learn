# 10. Bitwise Operators

- Work like the logical operators ([09_logical_operators.md](09_logical_operators.md)), but instead of acting on `True`/`False` values they apply the logic to every **bit** in a number, column by column
- In binary, `1` is like `True` and `0` is like `False`
- A **bit** is a single binary digit (`0` or `1`)

## Bitwise AND (`&`)

- "AND" is the name of the operation, the ampersand `&` is its symbol
- A column is `1` only when **both** numbers have a `1` in it

| a | b | `a & b` |
|---|---|---------|
| 0 | 0 | 0       |
| 1 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 1 | 1       |

**Example:** `0101 & 0010`

```text
  0101
& 0010
------
  0000
```

No column has a `1` in both numbers, so the result is `0000`.

```python
print(0b0101 & 0b0010)
# Prints 0

print(0b0101 & 0b0111)
# Prints 5 (0101 & 0111 = 0101)
```

## Other Bitwise Operators

| Operator | Name        | A column is `1` when...                  | Example           |
|----------|-------------|------------------------------------------|-------------------|
| `&`      | AND         | both numbers have a `1`                  | `5 & 3` is `1`    |
| `\|`     | OR          | at least one number has a `1`            | `5 \| 3` is `7`   |
| `^`      | XOR         | exactly one number has a `1`             | `5 ^ 3` is `6`    |
| `~`      | NOT         | (flips every bit of one number)          | `~5` is `-6`      |
| `<<`     | Left shift  | (moves bits left, doubles per place)     | `5 << 1` is `10`  |
| `>>`     | Right shift | (moves bits right, halves per place)     | `5 >> 1` is `2`   |

```text
  0101       0101       0101
| 0011     ^ 0011     & 0011
------     ------     ------
  0111       0110       0001
```

```python
print(5 | 3)
# Prints 7

print(5 ^ 3)
# Prints 6

print(~5)
# Prints -6 (~x is always -x - 1)

print(5 << 1)
# Prints 10

print(5 >> 1)
# Prints 2
```

*`|` is the pipe symbol, usually on the same key as backslash. `~` flips every bit, and because Python integers can be negative the result is `-x - 1`, not a short binary number.*
