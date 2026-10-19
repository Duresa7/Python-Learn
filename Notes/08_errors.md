# 8. Errors

## Syntax Error

- Code that breaks Python's rules for how code must be written
- Python can't understand it, so the program doesn't run at all
- Common causes: a missing quotation mark, a missing parenthesis, bad indentation

## Stack Trace

- The report Python prints when a program crashes
- Shows the file and line number where the error happened, the line of code itself, and the type of error with a message
- The error type and message are on the **last line**, so start reading there

## Example: Indentation Error

```python
def create_stats_message(strength, wisdom, dexterity):
      total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
    return msg
```

Output:

```text
File "main.py", line 3
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
                                                                                                                  ^
IndentationError: unindent does not match any outer indentation level
```

- `File "main.py", line 3` = where the error is
- `^` = where Python gave up reading the line
- `IndentationError: ...` = the error type and message. `IndentationError` is a more specific kind of `SyntaxError`.

*Line 2 is indented 6 spaces but line 3 is indented 4. Every line inside a function body must be indented by the same amount. (The f-string on line 3 is also missing its closing quote. Python reports the indentation problem first because it reads indentation before the rest of the line.)*
