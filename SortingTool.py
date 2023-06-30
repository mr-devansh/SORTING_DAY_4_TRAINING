# Read N and M from input
N, M = map(int, input().split())

# Read the sequence of N numbers
sequence = list(map(int, input().split()))

# Create a dictionary to store the counts of occurrences
counts = {}

# Update the counts of occurrences in the dictionary
for num in sequence:
    counts[num] = counts.get(num, 0) + 1

# Define a custom sorting key function
def custom_sort_key(num):
    return (-counts[num], sequence.index(num))

# Sort the sequence using the custom sorting key
sorted_sequence = sorted(sequence, key=custom_sort_key)

# Print the sorted sequence
for num in sorted_sequence:
    print(num, end=' ')
print()
