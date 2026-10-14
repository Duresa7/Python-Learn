# 2. Variables

## Creating and Using Variables

```python
message = "whatever we want"
print(message)
```

*No quotation marks in print(message) since message already has them.*

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

- All words must be lowercase and separated by underscores
- Can only contain letters, numbers, and underscores
- No spaces, use underscores instead
- Can never start with a number
  - `1_cool` → Bad
  - `cool_1` → Good
- Lowercase for normal variables, uppercase for unique variables
- Cannot use Python's own words, ex: `print`
- Short but descriptive

## Name Errors

You get a name error when:

- You forgot to assign the variable
- You spelled it differently
