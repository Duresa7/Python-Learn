# variable op= value, shortcut for variable = variable op value
star_rating = 4
star_rating -= 1  # same as star_rating = star_rating - 1
print(star_rating)  # 3

star_rating = 4
star_rating += 1
print(star_rating)  # 5

star_rating = 4
star_rating *= 2
print(star_rating)  # 8

star_rating = 4
star_rating /= 2  # division always gives a float
print(star_rating)  # 2.0
