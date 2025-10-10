from collections import defaultdict


# Function to count word frequencies using the defaultdict
def count_words(text):
    word_freq = defaultdict(int)
    for word in text.split():
        word_freq[word] += 1
    return word_freq


# Function to group items by their first letter
def group_by_first_letter(items):
    grouped = defaultdict(list)
    for item in items:
        grouped[item[0]].append(item)
    return grouped


# Function to initialize a nested dictionary using a default dict
def nested_defaultsect():
    return defaultdict(lambda: defaultdict(int))


# Function to display a default dict
def display_defaultsect(dd):
    for key, value in dd.items():
        print(f"{key}: {value}")


text = "apple banana apple orange banana apple"
word_counts = count_words(text)
print("Word Frequencies:")
display_defaultsect(word_counts)

items = ["apple", "apricot", "banana", "blueberry", "cherry"]
grouped_items = group_by_first_letter(items)
print("\nGrouped by First Letter:")
display_defaultsect(grouped_items)

nested = nested_defaultsect()
nested['fruits']['apple'] += 3
nested['fruits']['banana'] += 2
print("\nNested defaultdict:")
