arr = []

arr.insert(0, "item1")
print("Array after inserting an item at index 0:", arr)

# Remove an item by index
arr.pop(0)
print("Array after removing an item at index 0:", arr)

# Append an item to the end of the array
arr.append("item2")
print("Array after appending an item:", arr)

# Function to check for duplicate elements in the array
def check_duplicates(arr):
    return len(arr) != len(set(arr))

# Add some duplicate elements to the array
arr.append("item2")
arr.append("item3")
arr.append("item3")

# Check for duplicate elements
if check_duplicates(arr):
    print("Array contains duplicate elements.")
else:
    print("Array does not contain duplicate elements.")
