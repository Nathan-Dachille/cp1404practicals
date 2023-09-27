"""
Calculates the total price of n items.
A 10% discount applies for totals over $100.
"""

items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
total = 0
for i in range(items):
    price = float(input("Price of item: "))
    while price < 0:
        print(f"${price} is not a valid price!")
        price = float(input("Price of item: "))
    total = total + price
if total > 100:
    total = total * 0.9
print(f"Total price of {items} items is ${total:0.2f}")
