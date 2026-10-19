# 2. Variables

## Creating and Using Variables

```python
message = "whatever we want"
print(message)
```

*No quotation marks in `print(message)`. `message` is a variable name, so Python prints the value stored in it. With quotes, it would print the word message.*

```python
cool_kick = "I hate you"
print(cool_kick)
```

*cool_kick = variable, "I hate you" = string, print = function*

```python
cool_kickto = 2.00
print(cool_kickto)
```

*cool_kickto = variable, 2.00 = value, print = function*

## Naming Rules

- Use lowercase words separated by underscores
- Can only contain letters, numbers, and underscores
- No spaces, use underscores instead
- Can never start with a number
  - `1_cool` → Bad
  - `cool_1` → Good
- Lowercase for normal variables, ALL_CAPS for constants (values that never change)
- Don't use Python's own words, ex: `print` (a built-in) or `class` (a reserved word)
- Short but descriptive

## Name Errors

You get a name error when:

- You forgot to assign the variable
- You spelled it differently
