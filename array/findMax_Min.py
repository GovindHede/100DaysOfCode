
# Find Max / Min
numbers = [3,1,5,7,9,2]

print("Maximum number:", max(numbers))  # Output: Maximum number: 9
print("Minimum number:", min(numbers))  # Output: Minimum number: 1

# Manual Method 
max_val, min_val = numbers[0], numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max(Manual):",max_val)  # Output: Max(Manual): 9
print("Min(Manual):",min_val)  # Output: Min(Manual): 1