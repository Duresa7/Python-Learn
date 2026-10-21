# 4. Numbers and Math

## Integers

- Type name: `int`
- Simply: whole numbers, no decimals, positive or negative (`3` and `-3` are both integers)
- You store integers in a variable
- Dividing two integers with `/` always produces a float (see Floats below)

**Example:**

```python
apples = 5
candy = 10
total = apples + candy
print(total)
```

*apples = variable, 5 = int. Output: 15*

## Floats

- Type name: `float`
- The number type that allows decimal values

```python
my_int = 5
my_float = 5.5
```

*my_int = variable, 5 = int. my_float = variable, 5.5 = float*

## Math Syntax

| Operation      | Symbol | Example                   |
|----------------|--------|---------------------------|
| Addition       | `+`    | `message = 2 + 2`         |
| Subtraction    | `-`    | `test = 2 - 2`            |
| Multiplication | `*`    | `cool = 2 * 2`            |
| Division       | `/`    | `div = 2 / 2`             |
| Floor division | `//`   | `8 // 3`                  |
| Exponent       | `**`   | `2 ** 3`                  |
| Modulo         | `%`    | `13 % 3`                  |
| Parentheses    | `( )`  | `(message + test) / 3`    |
| Negative       | `-x`   | `candy = -420`            |

## Floor Division

- Like normal division, except the result is **floored** afterward: rounded **down** to the nearest integer
- Operator: `//`

```python
8 // 3
# 2 (an integer, rounded down from 2.666)

-7 // 3
# -3 (an integer, rounded down from -2.333)
```

*Rounding down means toward negative infinity, so -2.333 becomes -3, not -2.*

## Exponents

- Operator: `**`
- `2 ** 3` is `2^3`, which is `2 x 2 x 2 = 8`
- `3 ** 3` is `3 x 3 x 3 = 27`
- **Rule:** anything raised to the power of 0 equals 1
  - `5 ** 0` = 1
  - `x ** 0` = 1

## Modulo

- Operator: `%`
- Divides, then gives back the **remainder** instead of the answer
- `13 % 3` is `1`, because 13 = 4 × 3 + 1
- Works on floats too: `-25.5 % 2.25` is `1.5`
- Handy for even/odd: `n % 2` is `0` when `n` is even and `1` when it's odd

```python
print(13 % 3)
# Prints 1

print(10 % 2)
# Prints 0 (no remainder, so 10 is even)

print(-25.5 % 2.25)
# Prints 1.5
```

*A non-zero result has the same sign as the number on the right, which is why a negative number on the left can still give a positive answer.*

## In-Place Operators (Reassignment)

- Change a number variable by some amount, and store the result back in the same variable
- Also called incrementing (or decrementing) a variable

| Operation      | Operator |
|----------------|----------|
| Addition       | `+=`     |
| Subtraction    | `-=`     |
| Multiplication | `*=`     |
| Division       | `/=`     |

```python
star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0
```

*`star_rating -= 1` is the short way of writing `star_rating = star_rating - 1`. `/=` gives a float, so 2.0 and not 2.*

## Scientific Notation

- A way of writing very large or very small numbers
- Add the letter `e` (or `E`) followed by a positive or negative integer
- The exponent after the `e` says how many places to move the decimal point: **right** when positive, **left** when negative

**Example:** `2e3` means 2 × 10³, which equals 2,000.

| Part | Meaning                                                  |
|------|----------------------------------------------------------|
| `2`  | The starting number                                      |
| `e`  | "Times 10 to the power of"                               |
| `3`  | How many places to move the decimal (`e3` right, `e-3` left) |

*Tip for large numbers: count the digits and subtract 1 to get the exponent. `2000` has 4 digits, so it's `2e3`.*

```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

print(52.3E-4)
# Prints 0.00523 (a capital E works too)
```

*Scientific notation always produces a float.*

## Number Delimiter (Underscore)

- Use `_` inside a long number to make it easier to read
- Python ignores the underscores

```python
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```

## Binary Numbers

- **Base-10 (decimal)** uses 10 symbols: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
- **Base-2 (binary)** uses 2 symbols: `0` and `1`
- Syntax: start the number with `0b`. The prefix says what follows is binary
  - `0b10` is two, but `10` without the prefix is simply ten
- Python prints binary numbers as regular decimal numbers

```python
print(0b0001)
# Prints 1

print(0b0010)
# Prints 2

print(0b1010)
# Prints 10
```

*Each binary place is worth double the one to its right: 8, 4, 2, 1. So `0b1010` is 8 + 2 = 10.*

| Binary   | Decimal | Math          |
|----------|---------|---------------|
| `0b0101` | 5       | 4 + 1         |
| `0b0111` | 7       | 4 + 2 + 1     |

### Converting With `int()` and `bin()`

- `int()` can convert a binary **string** to an integer
- Its second argument is the base of the number (binary is base 2)
- `bin()` goes the other way: integer to a binary string starting with `0b`

```python
# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# Prints 4

print(bin(5))
# Prints 0b101
```

*`0b100` (no quotes) is already a number. `"100"` (in quotes) is a string, so it needs `int(..., 2)` to be read as binary. Without the `2`, `int("100")` is just one hundred.*

See [10_bitwise_operators.md](10_bitwise_operators.md) for doing math on the bits themselves.
