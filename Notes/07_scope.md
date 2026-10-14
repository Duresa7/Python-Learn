# Scope

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


global scope

1. Define a variable or function that can be accessible in every other place in the program
 this includes other functions
2. 