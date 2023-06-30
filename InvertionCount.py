def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)
    
    inversions = inv_left + inv_right + inv_merge
    return merged, inversions

def merge(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of the array
    n = int(input())
    # Read the elements of the array
    arr = list(map(int, input().split()))

    # Apply merge sort and count inversions
    _, inversions = merge_sort(arr)

    # Print the number of inversions
    print(inversions)
