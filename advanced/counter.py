# collections: Counter,numbed tuple,OrderDict,default dict,deque

from collections import Counter


# Function to count characters in a string
def count_characters(text):
    return Counter(text)


# Function to count words in a list
def count_words(word_list):
    return Counter(word_list)


# Function to merge two counters
def merge_counters(counter1, counter2):
    return counter1 + counter2


# Function to find the most common elements
def most_common_elements(counter, n=3):
    return counter.most_common(n)

text = "hello world"
words = ["apple", "banana", "apple", "orange", "banana", "banana"]

char_counter = count_characters(text)
word_counter = count_words(words)


print("Character Count:", char_counter)
print("Word Count:", word_counter)

merged = merge_counters(char_counter, word_counter)
print("Merged Counter:", merged)

print("Most Common in Word Counter:", most_common_elements(word_counter))
