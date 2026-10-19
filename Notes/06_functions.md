# 6. Functions

## What a Function Is

- A reusable block of code that does a specific job
- **Parameters** are the named inputs a function takes, written inside the `( )` when you define it
- **Arguments** are the actual values you pass in when you call it

## Function Rules

- It can take zero or more inputs inside `( )`
- The code after `:` must be indented to form the function body
- It can return a value, which you can store in a variable
- Prefer `return` over `print` inside a function, so the caller can use the result
- Define a function before you call it, so define all the functions first

## Defining and Calling a Function

**Step 1: Define the function**

```python
def say_hello():
    print("Hello")
```

*The ( ) holds the parameters or arguments.*

**Step 2: Call the function**

```python
say_hello()
```

*Output: Hello*

## Parameters

- Default value: can be used when you have an optional parameter
- Operator: `=`
- If the caller doesn't pass that argument, the default is used in its place

```python
def greet(name="friend"):
    print(f"Hello, {name}")


greet()
# Prints Hello, friend

greet("Sam")
# Prints Hello, Sam
```

## Return

- Provides a value back to the caller of the function
- The function stops as soon as it hits `return`
- A function with no `return` gives back `None`

## Full Breakdown Example

```python
def tropical_candy(r):
    pi = 3.14
    message = 10
    result = pi * message * r * r
    return result

print(tropical_candy(5))
# Prints 785.0
```

| Part               | Code                | What it is                          |
|--------------------|---------------------|-------------------------------------|
| Function           | `tropical_candy`    | The name of the function            |
| Parameter          | `r`                 | Whatever you want r to be (here, 5) |
| Variables          | `pi`, `message`     | Values stored inside the function   |
| Parameter variable | `r * r`             | The parameter used in the math      |
| Return             | `return result`     | Provides the output                 |
| Variable           | `result`            | Holds the answer that gets returned |

- `tropical_candy(5)` calls the function and passes `5` in for `r`
