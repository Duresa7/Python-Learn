# 7. Scope

**Scope** is where a variable or function name is available to use.

Think of it like a permissions hierarchy. For example, an IT admin can use their login on any PC in the office, while an end user can only use theirs on their specific PC.

## Example

```python
def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"
```

When the `subtract` function is called, we assign `5` to the variable `x`, but `x` only exists inside the function. If we try to print `x` outside of that function, we get an error (a `NameError`) instead of a result.

## Key Points

- Variables created inside a function are **local**. They only exist while the function runs.
- Code outside the function can't see them.

## Global Scope

- A variable or function defined outside of any function is in the **global scope**
- It can be accessed from every other place in the program, including inside other functions

```python
greeting = "Hello"


def say_greeting():
    print(greeting)


say_greeting()
# Prints Hello
```

*greeting = global variable. say_greeting can read it even though it was defined outside the function.*

| Scope  | Where it's defined   | Where it can be used           |
|--------|----------------------|--------------------------------|
| Local  | Inside a function    | Only inside that function      |
| Global | Outside any function | Anywhere in the program        |
