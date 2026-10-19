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
