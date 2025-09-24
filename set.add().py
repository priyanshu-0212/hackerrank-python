# Create an empty set
unique_items = set()

# Number of elements (could come from input)
n = int(input())

# Loop to read each item
for _ in range(n):
    item = input()       # Read the element (string, number, etc.)
    unique_items.add(item)  # Add it to the set

# Print the number of unique items
print(len(unique_items))
