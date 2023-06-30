def sortArray(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of the array
    n = int(input())
    # Read the elements of the array
    arr = list(map(int, input().split()))

    # Sort the array using the two-pointer technique
    sorted_arr = sortArray(arr)

    # Print the sorted array
    for num in sorted_arr:
        print(num, end=' ')
    print()
