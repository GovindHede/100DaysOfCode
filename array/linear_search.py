def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 # Target not found
#     0    1   2  3    4
arr= [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element 30 found at index: 2

# Algorithm of Linear Search
#1.Start from the first element and compare it with the target.
#2.If you find the target, return its index.
#3.If not, keep moving through the array until the end.
#
