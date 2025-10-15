# Prefix Sum Array

arr = [1, 2, 3, 4, 5]
prefix = [0] * len(arr)  #prefix = [0, 0, 0, 0, 0]
prefix[0] = arr[0]
# prefix[0] = 1
# prefix = [1, 0, 0, 0, 0]
for i in range(1,len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("prefix sum array:", prefix)  # Output: [1, 3, 6, 10, 15]

# We calculate each prefix[i] step by step:

# i = 1:
# prefix[1] = prefix[0] + arr[1] = 1 + 2 = 3
# → prefix = [1, 3, 0, 0, 0]

# i = 2:
# prefix[2] = prefix[1] + arr[2] = 3 + 3 = 6
# → prefix = [1, 3, 6, 0, 0]

# i = 3:
# prefix[3] = prefix[2] + arr[3] = 6 + 4 = 10
# → prefix = [1, 3, 6, 10, 0]

# i = 4:
# prefix[4] = prefix[3] + arr[4] = 10 + 5 = 15
# → prefix = [1, 3, 6, 10, 15]


# Query: Sum from index 1 to 3
l,r = 1,3
range_sum= prefix[r] - (prefix[l - 1] if l > 0 else 0)
print("sum from index 1 to 3:", range_sum)  # Output: 9