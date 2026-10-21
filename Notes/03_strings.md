# 3. Strings

## String Rules

- Characters strung together, wrapped in quotation marks
- Single or double quotes work (double is preferred)

## F-Strings

- Used to put variables inside a string
- Always add `f` before the quotation marks
- Variables must be inside `{ }`

**Example:**

```python
candy = "bots"
toy = 5

print(f"string of {toy} to many {candy}")
```

*f = f-string, {toy} = variable #1, {candy} = variable #2*

- F-strings can be assigned to a variable

**Example:**

```python
choco = f"{total_bot} of the"
return choco
```

## The `format()` Method

- An older way to put variables inside a string (before f-strings). Still common in older code
- Put `{}` where each value goes, then call `.format()` on the string with the values inside the `( )`
- The values fill the `{}` in order, left to right

```python
age = 20
name = "Swaroop"

print("{} was {} years old when he wrote this book".format(name, age))
# Prints Swaroop was 20 years old when he wrote this book

print("Why is {} playing with that python?".format(name))
# Prints Why is Swaroop playing with that python?
```

*Same result with an f-string: `print(f"{name} was {age} years old when he wrote this book")`. F-strings are preferred because the variable sits right where it's used.*

*(Even older still is `%` string formatting, like `"%s is %d" % (name, age)`. You'll see it in very old code, but you don't need it.)*

## Changing How `print()` Ends

- `print()` adds a newline at the end by default, so the next `print()` starts on a new line
- The `end=` argument changes what gets printed at the end instead

```python
print("a", end=" ")
print("b", end=" ")
print("c")
# Prints a b c
```

*The first two prints end with a space instead of a newline, so everything lands on one line.*

## Continuing a String on the Next Line

- A backslash `\` at the very end of a line continues the string on the next line

```python
s = "This is a string. \
This continues the string."
print(s)
# Prints This is a string. This continues the string.
```

- Nothing can come after the `\`, not even a space, or it won't work
- Don't indent the next line. Any spaces at its start become part of the string
- The space before the `\` is part of the string too, which is why "string." and "This" are separated
