from collections import Counter

list_counter = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7]

#  this is a dict where the key is the actual value and the value is the key
print(Counter(list_counter))

# this is another way of getting the count of the words in the sentence

words = "This is for testing the word in the word of word of the sentence of the sentence of the word"

word_split = words.lower().split()

print(Counter(word_split))
