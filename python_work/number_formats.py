# Scientific notation: number e exponent
# Positive exponent moves the decimal right, negative moves it left
print(16e3)    # 16000.0 (16 with the decimal moved 3 places right)
print(7.1e-2)  # 0.071 (7.1 with the decimal moved 2 places left)

# Delimiter: underscores make big numbers easier to read, Python ignores them
num = 16_000
print(num)  # 16000

num = 16_000_000
print(num)  # 16000000

# Binary: base-2, only the symbols 0 and 1. Start the number with 0b
# Python prints it as a regular decimal number
print(0b0001)  # 1
print(0b0010)  # 2
print(0b1010)  # 10 (8 + 2)

# int(string, 2) converts a binary string to an integer (2 = base 2)
binary_string = "100"
num = int(binary_string, 2)
print(num)  # 4
print(int("100"))  # 100, without the base it's read as decimal

# bin() goes the other way: integer to binary string
print(bin(5))  # 0b101
