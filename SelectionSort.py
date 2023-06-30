def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of the array
    n = int(input())
    # Read the elements of the array
    arr = list(map(int, input().split()))

    # Perform selection sort
    selection_sort(arr)

    # Print the sorted order
    for num in arr:
        print(num, end=' ')
    print()
