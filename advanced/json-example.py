import json

# Python dictionary
data = {
    "name": "Sachin Tentacular",
    "role": "Staff Software Engineer",
    "location": "Pune, MH",
    "skills": ["Python", "LangGraph", "FAISS", "RAG"]
}

# Convert Python dict to JSON string
json_string = json.dumps(data, indent=4)
print("JSON String:")
print(json_string)

# Convert JSON string back to Python dict
parsed_data = json.loads(json_string)
print("\nParsed Python Dictionary:")
print(parsed_data)

# Read JSON from a file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print("\nLoaded from file:")
    print(loaded_data)
