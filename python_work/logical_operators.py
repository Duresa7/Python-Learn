# and: both sides must be True
print(True and True)    # True (the only way and is True)
print(True and False)   # False
print(False and False)  # False

# or: at least one side must be True
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False (the only way or is False)

# not: reverses the value
print(not True)   # False
print(not False)  # True

# Parentheses group conditions
print((True or False) and False)  # False

# Without parentheses: not first, then and, then or
print(True or False and False)  # True, because and runs first
