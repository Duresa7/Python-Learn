# Comparison operators compare two values and give back a Boolean
print(3 < 5)    # True, less than
print(3 > 5)    # False, greater than
print(5 <= 5)   # True, less than or equal to
print(5 >= 6)   # False, greater than or equal to
print(5 == 5)   # True, equal to
print(5 != 5)   # False, not equal to

# One = stores a value, two == compares two values
x = 5
print(x == 5)  # True

# They work on strings too, and the comparison is case-sensitive
print("cat" == "cat")  # True
print("cat" == "Cat")  # False


def player_1_wins(player_1_score, player_2_score):
    winner = player_1_score > player_2_score
    return winner


print(player_1_wins(10, 7))  # True
print(player_1_wins(3, 7))   # False


def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same


print(compare_heights(165, 165, 160, 165))  # (True, True, False)


def can_withstand_blow(hero_armor, enemy_damage):
    survives = hero_armor >= enemy_damage
    return survives


print(can_withstand_blow(50, 50))  # True
print(can_withstand_blow(40, 50))  # False
