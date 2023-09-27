# Task 1
name = input("What is your name? ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Task 2
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name.strip()}.")

# Task 3
in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(f"{first_number + second_number}")

# Task 4
in_file = open("numbers.txt", 'r')
sum = 0
for line in in_file:
    sum += float(line)
in_file.close()
print(f"The sum of the numbers in numbers.txt is {sum}.")
