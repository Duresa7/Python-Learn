# 12. If Statements

## `if`

- Runs code only when a condition is met (the condition is a Boolean, usually from a [comparison](11_comparison_operators.md))
- The colon `:` after the condition is required
- Indentation tells Python which code is inside the `if` and where it ends

```python
if CONDITION:
    # do some stuff here

# code after the if block still runs, no matter what
```

**Example:**

```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")


show_status(10)
# Prints Ganondorf is alive!

show_status(0)
# Prints Ganondorf is unalive!
```

*When the condition is `True`, the function prints and hits `return`, so it stops before the last line.*

Code that is **not** indented under the `if` runs either way:

```python
def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")


print_status(0)
# Prints dead, then status check complete

print_status(10)
# Prints status check complete
```

## `elif` and `else`

- `elif` means "else if". It checks another condition when the ones before it were `False`
- `else` runs when none of the conditions above were `True`
- Python goes from top to bottom and runs **only the first branch** that is `True`

```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
```

**Example:**

```python
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"


print(player_status(3))
# Prints injured
```

*`health` is 3, so `health <= 0` is `False` and `health <= 5` is `True`. Python returns `"injured"` and never looks at `else`.*

## Rules

- An `if` can be followed by **zero or more** `elif` statements, then **zero or one** `else`
- You can't have an `elif` or an `else` without an `if` before it
- You can have an `else` without any `elif`

```python
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
```

*An `if` with several `elif`s and an `else`:*

```python
def check_score_rank(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
```
