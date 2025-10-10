
#Define two sets of programming languages

backend_languages = {"Python", "Java", "Go", "Rust"}
frontend_languages = {"JavaScript", "TypeScript", "HTML", "CSS"}


# Function to add a language to a set
def add_language(language_set, language):
    language_set.add(language)
    print(f"Added {language} to the set.")


# Function to remove a language from a set
def remove_language(language_set, language):
    if language in language_set:
        language_set.remove(language)
        print(f"Removed {language} from the set.")
    else:
        print(f"{language} not found in the set.")


# Function to find common languages (intersection)
def common_languages(set1, set2):
    return set1.intersection(set2)


# Function to find all unique languages (union)
def all_languages(set1, set2):
    return set1.union(set2)


# Function to find languages only in the backend (difference)
def backend_only(set1, set2):
    return set1.difference(set2)


# Example usage
add_language(backend_languages, "Node.js")
remove_language(frontend_languages, "HTML")


print("Common languages:", common_languages(backend_languages, frontend_languages))
print("All languages:", all_languages(backend_languages, frontend_languages))
print("Languages only in backend:", backend_only(backend_languages, frontend_languages))
