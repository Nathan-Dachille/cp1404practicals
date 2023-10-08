"""Asks for and stores email addresses and names.
Estimate: 20
Actual:
"""


def main():
    """Store email addresses and names to dictionary."""
    emails_to_name = dict()
    email = input("Email: ")
    while email != '':
        name = get_name_from_email(email)
        keep_name = input(f"Is {name} your name? [Y/n] ").upper()
        if keep_name == 'Y' or keep_name == '':
            emails_to_name[email] = name
        else:
            name = input("Name: ")
            emails_to_name[email] = name
        email = input("Email: ")
    print_details(emails_to_name)


def get_name_from_email(email:str) -> str:
    """Get a name from start of email."""
    username = email.split("@")[0]
    if '.' in username:
        name = ' '.join(username.split('.'))
        return name.title()
    else:
        return username


def print_details(details: dict):
    """Print Names and Email addresses."""
    for email in details:
        print(f"{details[email]} ({email})")


main()
