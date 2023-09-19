"""Gets a password of min_length and returns asterisks."""


def main():
    """Main function for password_stars."""
    password = get_password(min_length=8)
    print_asterisks(password)


def print_asterisks(string):
    """Prints asterisks for the length of a given string."""
    print("*" * len(string))


def get_password(min_length):
    """Gets a password that is at least min_length."""
    password = ""
    while len(password) < min_length:
        print(f"Password needs to be at least {min_length} characters long.")
        password = input("Please enter a valid password: ")
    return password


main()
