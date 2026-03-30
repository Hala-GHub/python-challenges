# Challenge 1 — Build a Profile
# Create a dictionary for a person with keys "name", "age",
# and "city", then print each value using get().
# Method: get()
# --------------------------------------------------------------

profile = {}
profile["name"] = "Hala"
profile["age"] = 30
profile["city"] = "Calgary"

print(profile.get("name"))
print(profile.get("age"))
print(profile.get("city"))

# --------------------------------------------------------------
# Challenge 2 — Safe Access
# Retrieve "email" safely — it doesn't exist, so return
# "not provided" as the default instead.
# Method: get()
# --------------------------------------------------------------

user = {"name": "Bob", "age": 25}
email =  user.get("email", "not provided")
print(email)

# --------------------------------------------------------------
# Challenge 3 — Update the Record
# Update "age" to 26 and add a new key "job" with value "Dev",
# both in a single call. Then print the updated dict.
# Method: update()
# --------------------------------------------------------------

record = {"name": "Bob", "age": 25}
record.update({"age": 26,"job": "Dev"})
print(record)

# --------------------------------------------------------------
# Challenge 4 — Set Only If Missing
# Set "theme" to "light" only if it doesn't already exist,
# then try to overwrite "lang" — it should NOT change.
# Method: setdefault()
# --------------------------------------------------------------

config = {"lang": "en", "debug": False}
config.setdefault("theme", "light")
config.setdefault("lang","fr")
print(config)

# --------------------------------------------------------------
# Challenge 5 — Remove and Reuse
# Pop "city" from the dict, store its value in a variable,
# then print both the removed value and the remaining dict.
# Method: pop()
# --------------------------------------------------------------

employee = {"name": "Alice", "age": 30, "city": "Toronto"}

city =employee.pop("city")
print(city)
print(employee)


# Challenge 6 — Inspect the Dictionary
# Print all keys, all values, and all key-value pairs of the
# dict below using the three view methods.
# Methods: keys(), values(), items()
# --------------------------------------------------------------

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
print(inventory.keys())
print(inventory.values())
print(inventory.items())

 --------------------------------------------------------------
# Challenge 7 — Merge Preferences
# Merge defaults and user_prefs so that user_prefs values win
# on conflict. Store the result in a new dict called "final".
# Method: | operator (Python 3.9+) or {**a, **b}
# --------------------------------------------------------------

defaults   = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark", "lang": "fr"}
final ={**defaults, **user_prefs}
print(final)

# --------------------------------------------------------------
# Challenge 8 — Initialize from a List
# Create a dict where each subject is a key and its default
# grade value is 0.
# Method: dict.fromkeys()
# --------------------------------------------------------------

subjects = ["math", "science", "history", "art"]
grades =dict.fromkeys(subjects,0)
print(grades)

# --------------------------------------------------------------
# Challenge 9 — Count Word Frequency
# Count how many times each word appears in the list below.
# Build the result dict using get() inside a loop.
# Method: get()
# --------------------------------------------------------------

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)

 --------------------------------------------------------------
# Challenge 10 — Sort by Value
# Sort the scores dict by score from highest to lowest and
# rebuild it as a new sorted dict. Print the final result.
# Method: sorted() with key + dict()
# --------------------------------------------------------------

scores = {"Bob": 88, "Alice": 95, "Charlie": 72, "Diana": 90}

sorted_scores = dict(
    sorted(scores.items(), key=lambda item: item[1], reverse=True)
)

print(sorted_scores)

