def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)

def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Usage
for line in read_large_file('data-text.txt'):
    print(line)


def paginate(items, page_size):
    """Yield pages of items with a fixed page size."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

# Sample data
movies = [
    "Inception", "The Matrix", "Interstellar", "Parasite", "The Dark Knight",
    "Fight Club", "Forrest Gump", "Pulp Fiction", "The Godfather", "Gladiator"
]

# Use the generator
for page_number, page in enumerate(paginate(movies, 3), start=1):
    print(f"Page {page_number}: {page}")