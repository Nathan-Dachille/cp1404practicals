"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the input is not a number.
2. When will a ZeroDivisionError occur?
    When denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Don't allow the denominator to be equal to 0.
"""

is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be 0!")
        else:
            is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
# Error will never occur
fraction = numerator / denominator  # type: ignore
print(fraction)
