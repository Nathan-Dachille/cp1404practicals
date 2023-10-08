"""Counts the occurrences of if words in a string.
Estimate: 20 minutes
Actual:   16 minutes
"""

text = input("Enter a string: ").lower()

words = text.split(" ")

word_to_count = dict()

for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

print(f"Text: {text}")
for word in word_to_count:
    print(f"{word} : {word_to_count[word]}")
