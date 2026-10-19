# 1. Key Terms

- Strings are text. Example: `"Hello"`
- Values are the data itself: numbers, text, and so on. Example: `5`, `2.00`, `"Hello"`
- Functions are actions. Example: `print`
- Variables are names that refer to a value. Think of variables as labels you stick on values.

**Example:**

```python
x = 5
```

*x = the variable, 5 = the value*

## Quick Definitions

Short versions of terms that have their own notes.

- **Integer:** a whole number, positive or negative. Example: `3`, `-3` → [04_numbers_and_math.md](04_numbers_and_math.md)
- **Float:** a number with a decimal point. Example: `5.5`
- **Floor division (`//`):** divide, then round down to the nearest integer. Example: `8 // 3` is `2`
- **Exponent (`**`):** multiply a number by itself that many times. Example: `2 ** 3` is `8`. Anything `** 0` is `1`
- **In-place operator (`+=`, `-=`, `*=`, `/=`):** change a variable and store the result back in it
- **Scientific notation:** `e` followed by how many places to move the decimal. Example: `16e3` is `16000.0`
- **Delimiter (`_`):** underscore inside a number for readability. Example: `16_000`
- **Binary:** base-2 numbers that only use `0` and `1`. Start with `0b`. Example: `0b1010` is `10` → [04_numbers_and_math.md](04_numbers_and_math.md)
- **Boolean:** a value that is either `True` or `False` → [09_logical_operators.md](09_logical_operators.md)
- **Logical operators (`and`, `or`, `not`):** combine or reverse Boolean values
- **Bit:** a single binary digit, `0` or `1`
- **Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`):** apply logic to every bit of a number, column by column → [10_bitwise_operators.md](10_bitwise_operators.md)
- **Scope:** where a name is available to use → [07_scope.md](07_scope.md)
- **Global scope:** defined outside any function, so usable everywhere in the program
- **Syntax error:** code that breaks Python's rules, so it can't run → [08_errors.md](08_errors.md)
- **Stack trace:** the report Python prints when a program crashes, error type on the last line
