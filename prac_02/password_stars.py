MIN_LENGTH = 8

password = ""
while len(password) < MIN_LENGTH:
    print(f"Password needs to be at least {MIN_LENGTH} characters long.")
    password = input("Please enter a valid password: ")
print("*" * len(password))
