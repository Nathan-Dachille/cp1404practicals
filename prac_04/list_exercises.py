
# Basic list operations.
numbers = []

while len(numbers) < 5:
    numbers.append(int(input("Number: ")))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/5:.2f}")

# Woefully inadequate security checker.

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_input = input("Enter your username: ")

if username_input in usernames:
    print("Access granted.")
else:
    print("Access denied.")
