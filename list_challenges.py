# Challenge 1 — Build Your Grocery List
# Start with an empty list. Add "eggs", "milk", and "bread"
# one at a time, then print the final list.
# Method: append()
# Challenge 1:  Call append() three times, once per item.
# --------------------------------------------------------------

grocery = []
grocery.append("eggs")
grocery.append("milk")
grocery.append("bread")
print(grocery)

# --------------------------------------------------------------
# Challenge 2 — Merge the Shelves
# Combine shelf_b into shelf_a WITHOUT creating a new list,
# then print the result.
# Method: extend()
# Challenge 2:  extend() adds all items from another iterable in place.
# --------------------------------------------------------------

shelf_a = ["pasta", "rice"]
shelf_b = ["beans", "lentils", "oats"]
shelf_a.extend(shelf_b)
print(shelf_a)

# --------------------------------------------------------------
# Challenge 3 — VIP Guest
# Insert "Diana" at position 1 so she appears second.
# Method: insert()
# Challenge 3:  insert(index, value) shifts existing items to the right.
# --------------------------------------------------------------

guests = ["Alice", "Bob", "Charlie"]
guests.insert(1, "Diana")
print(guests)

# --------------------------------------------------------------
# Challenge 4 — Remove the Duplicate
# Remove the FIRST occurrence of 7 and print the updated list.
# Method: remove()
# Challenge 4:  remove() only deletes the first match — the second 7 stays.
# --------------------------------------------------------------

numbers = [4, 7, 2, 7, 9]
numbers.remove(7)
print(numbers)

 --------------------------------------------------------------
# Challenge 5 — Stack Simulation
# Push 10, 20, 30 onto a stack (list), then pop the top two
# items and print each popped value.
# Methods: append(), pop()
# Challenge 5:  Stack is last-in first-out; pop() with no argument removes the last item.
# --------------------------------------------------------------

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())  # Pops 30
print(stack.pop())  # Pops 20


# --------------------------------------------------------------
# Challenge 6 — Sort the Scores
# Sort scores from HIGHEST to LOWEST and print the result.
# Method: sort(reverse=True)
# Challenge 6:  Pass reverse=True to sort() for descending order.
# --------------------------------------------------------------

scores = [88, 45, 92, 67, 73]
scores.sort (reverse=True)
print(scores)

# --------------------------------------------------------------
# Challenge 7 — Alphabetical, but Fair
#ort the list below case-insensitively.
# Method: sort(key=str.lower)
# Challenge 7:  Without key=str.lower, uppercase letters sort before lowercase due to ASCII values.
# --------------------------------------------------------------

words = ["banana", "Apple", "cherry", "Mango"]
words.sort(key=str.lower)
print(words)

# --------------------------------------------------------------
# Challenge 8 — Find & Count
# 1. How many times does "yes" appear?
# 2. What is the index of the first "no"?
# Methods: count(), index()
# Challenge 8:  count() gives total occurrences; index() returns the position of the first match.
# --------------------------------------------------------------

votes = ["yes", "no", "yes", "yes", "no", "yes"]
print (votes.count("yes")) 
print (votes.index("no"))

# --------------------------------------------------------------
# Challenge 9 — Reverse Without Sorting
# Reverse the list IN PLACE and print it.
# Method: reverse()
# Challenge 9:  reverse() returns None — don't assign its result to a variable.
# --------------------------------------------------------------

letters = ["a", "b", "c", "d", "e"]
letters.reverse()
print(letters)

# --------------------------------------------------------------
# Challenge 10 — Sort Without Touching the Original
# Create a new sorted list (ascending) while keeping temps
# unchanged, then print both to verify.
# Method: sorted()
# Challenge 10: Unlike sort(), sorted() never modifies the original list.
# --------------------------------------------------------------

temps = [36.6, 37.2, 35.9, 38.1, 36.0]
sorted_temps = sorted(temps)
print(temps)
print(sorted_temps)
