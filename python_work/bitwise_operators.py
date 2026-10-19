# Bitwise operators work on every bit of a number, column by column
# 0b0101 is 5, 0b0011 is 3

# & (AND): a column is 1 only when both numbers have a 1
print(0b0101 & 0b0010)  # 0
print(0b0101 & 0b0111)  # 5

# | (OR): a column is 1 when at least one number has a 1
print(5 | 3)  # 7  (0101 | 0011 = 0111)

# ^ (XOR): a column is 1 when exactly one number has a 1
print(5 ^ 3)  # 6  (0101 ^ 0011 = 0110)

# ~ (NOT): flips every bit, always gives -x - 1
print(~5)  # -6

# << and >>: shift the bits left or right
print(5 << 1)  # 10 (doubles)
print(5 >> 1)  # 2  (halves, rounded down)

# bin() shows the binary version of a number
print(bin(5 & 3))  # 0b1
print(bin(5 | 3))  # 0b111
