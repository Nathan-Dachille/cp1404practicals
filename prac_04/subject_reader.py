"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Reads subject information from a text document and prints it."""
    data = get_data()
    for part in data:
        print(
            f"{part[0]} is taught by {part[1]} and has {part[2]} students.")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer (ignore PyCharm's warning)
        parts[2] = int(parts[2])  # type: ignore
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


main()
