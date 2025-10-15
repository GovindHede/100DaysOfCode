# what is the sorting 
# Sorting means rearranging elements in increasing or decreasing order.
#Python has a built-in function sorted().
# Example usage

numbers = [5, 2, 9, 1, 5, 6]

print("sorting Ascending:", sorted(numbers)) # Output: [1, 2, 5, 5, 6, 9]
print("sorting Descending:", sorted(numbers, reverse=True))  # Output: [9, 6, 5, 5, 2, 1]


# Manual Method Bubble Sort
arr = [5,2,8,1,3]
n= len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(" Bubble Sorted Array:", arr)  # Output: Sorted Array: [1, 2, 3, 5, 8]
