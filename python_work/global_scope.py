# greeting is defined outside any function, so it's in the global scope
greeting = "Hello"


def say_greeting():
    # Functions can read global variables
    print(greeting)


say_greeting()  # Hello
print(greeting)  # Hello, it works outside the function too
