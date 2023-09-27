import random

print(random.randint(5, 20))  # line 1
# The smallest posible number is 5 and the largest is 20.

print(random.randrange(3, 10, 2))  # line 2
# The smallest posible number is 3 and the largest is 9.
# 4 cannot be made as it is even.

print(random.uniform(2.5, 5.5))  # line 3
# The smallest posible number is 2.5 and largest is 5.5 if rounded up.

print(random.randint(1, 100))
