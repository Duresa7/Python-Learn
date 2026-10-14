# 6. Functions

## What a Function Is

- A reusable codeblock that can do a specific job
- Parameters are how many times we call the function

## Function Rules

- It takes one input `( )`
- The code after `:` must be indented to form the function body
- It returns a single value that you store in a variable
- Print is rarely used when submitting work
- Order of functions: define all the functions first

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

*Output: Hello!*

## Parameters

- Default value: can be used when you have an optional parameter
- Operator: `=`
- If you have nothing defined, the default is used in its place as a result

## Return

- Provides a value back to the caller of the function
- Useful for debugging; it lets you see what values are stored in various variables

## Full Breakdown Example

```python
def tropical_candy(r):
    pi = 3.14
    message = 10
    result = pi * message * r * r
    return result

print(tropical_candy(5))
```

| Part               | Code                | What it is                          |
|--------------------|---------------------|-------------------------------------|
| Function           | `tropical_candy`    | The name of the function            |
| Parameter          | `r`                 | Whatever you want r to be (here, 5) |
| Variables          | `pi`, `message`     | Values stored inside the function   |
| Parameter variable | `r * r`             | The parameter used in the math      |
| Return             | `return result`     | Provides the output                 |
| Variable           | `result`            | The variable used to call it        |

- You use `tropical_candy(r)` to call it and define r
