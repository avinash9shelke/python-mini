# Strings: ordered, immutable, text representation

# Define a string
text = "  Hello, Python World!  "

# 1. strip() - Removes leading and trailing whitespaces
cleaned_text = text.strip()
print("Stripped Text:", cleaned_text)

# 2. lower() - Converts all characters to lowercase
lower_text = cleaned_text.lower()
print("Lowercase:", lower_text)

# 3. upper() - Converts all characters to uppercase
upper_text = cleaned_text.upper()
print("Uppercase:", upper_text)

# 4. replace() - Replaces a substring with another
replaced_text = cleaned_text.replace("Python", "Programming")
print("Replaced Text:", replaced_text)

# 5. split() - Splits the string into a list based on a delimiter
words = cleaned_text.split(" ")
print("Split Words:", words)

# 6. find() - Finds the index of the first occurrence of a substring
index = cleaned_text.find("Python")
print("Index of 'Python':", index)

# 7. len() - Returns the length of the string
length = len(cleaned_text)
print("Length of String:", length)
