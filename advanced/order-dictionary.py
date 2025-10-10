
from collections import OrderedDict

# Function to create an OrderedDict from a list of key-value pairs
def create_ordered_dict(pairs):
    return OrderedDict(pairs)

#Function to add a new item to the OrderedDict
def add_item(odict, key, value):
    odict[key] = value
    return odict

# Function to move an item to the end or beginning
def move_item(odict, key, to_end=True):
    odict.move_to_end(key, last=to_end)
    return odict

# Function to delete an item
def delete_item(odict, key):
    if key in odict:
        del odict[key]
    return odict

# Function to display the OrderedDict
def display_ordered_dict(odict):
    for key, value in odict.items():
        print(f"{key}: {value}")

items = [('apple', 3), ('banana', 5), ('orange', 2)]
od = create_ordered_dict(items)

print("Original OrderedDict:")
display_ordered_dict(od)

print("\nAfter adding 'grape':")
add_item(od, 'grape', 4)
display_ordered_dict(od)

print("\nAfter moving 'banana' to the end:")
move_item(od, 'banana', to_end=True)
display_ordered_dict(od)

print("\nAfter deleting 'apple':")
delete_item(od, 'apple')
display_ordered_dict(od)



