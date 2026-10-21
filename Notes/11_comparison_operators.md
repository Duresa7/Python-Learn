# 11. Comparison Operators

- Used to compare two values
- The result is always a Boolean (`True` or `False`), so these work together with [09_logical_operators.md](09_logical_operators.md)
- Work on numbers and on strings

| Operator | Meaning                  | Example   | Result  |
|----------|--------------------------|-----------|---------|
| `<`      | less than                | `3 < 5`   | `True`  |
| `>`      | greater than             | `3 > 5`   | `False` |
| `<=`     | less than or equal to    | `5 <= 5`  | `True`  |
| `>=`     | greater than or equal to | `5 >= 6`  | `False` |
| `==`     | equal to                 | `5 == 5`  | `True`  |
| `!=`     | not equal to             | `5 != 5`  | `False` |

## `=` vs `==`

- One `=` **stores** a value in a variable
- Two `==` **compare** two values and give back `True` or `False`
- String comparisons are case-sensitive: `"cat" == "Cat"` is `False`

## Examples

Store the comparison in a variable, then return it:

```python
def player_1_wins(player_1_score, player_2_score):
    winner = player_1_score > player_2_score
    return winner


print(player_1_wins(10, 7))
# Prints True
```

*`player_1_score > player_2_score` is the comparison. `winner` holds the Boolean result.*

A function can return several values at once, separated by commas:

```python
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same


print(compare_heights(165, 165, 160, 165))
# Prints (True, True, False)
```

*Returning several values gives them back together as a tuple, in the order written.*

```python
def can_withstand_blow(hero_armor, enemy_damage):
    survives = hero_armor >= enemy_damage
    return survives


print(can_withstand_blow(50, 50))
# Prints True (>= includes equal)
```

Next: [12_if_statements.md](12_if_statements.md) uses these comparisons to decide what code runs.
