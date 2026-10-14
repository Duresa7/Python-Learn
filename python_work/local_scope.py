def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(result)

# x only exists inside subtract, so this line gives a NameError.
# Remove the # to see it happen.
# print(x)
