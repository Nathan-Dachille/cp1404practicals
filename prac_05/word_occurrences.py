"""Counts the occurrences of if words in a string.
Estimate: 20 minutes
Actual:   30 minutes
"""

text = input("Enter a string: ").lower()
words = text.split(" ")
word_to_count = dict()

longest_word = ""
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1
    if len(word) > len(longest_word):
        longest_word = word

print(f"Text: {text}")
for word in sorted(word_to_count.keys()):
    print(f"{word:{len(longest_word)}} : {word_to_count[word]}")
