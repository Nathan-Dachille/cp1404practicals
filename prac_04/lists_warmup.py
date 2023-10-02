numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] == 3
# numbers[-1] == 2
# numbers[3] == 1
# numbers[:-1] == [3, 1, 4, 1, 5, 9]
# numbers[3:4] == [1]
# 5 in numbers == 1
# 7 in numbers == 0
# "3" in numbers == 0
# numbers + [6, 5, 3] == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"  # type: ignore
numbers[-1] = 1
print(numbers[2:])
print("9 is an element of numbers:", bool(9 in numbers))
