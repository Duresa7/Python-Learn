# .format() fills each {} with the arguments, in order
age = 20
name = "Swaroop"
print("{} was {} years old when he wrote this book".format(name, age))
print("Why is {} playing with that python?".format(name))

# The f-string version of the same thing (newer, preferred)
print(f"{name} was {age} years old when he wrote this book")

# print() ends with a newline by default. end= changes what it ends with
print("a", end=" ")
print("b", end=" ")
print("c")  # a b c, all on one line

# A backslash at the very end of a line continues the string on the next line
s = "This is a string. \
This continues the string."
print(s)  # This is a string. This continues the string.
