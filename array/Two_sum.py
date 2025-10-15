# write two sum code 
def two_sum(nums, target):
    seen = {} # store number :index
    for i , num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return []
print(two_sum([2,7,11,15], 9))  # Output: [0, 1]
# Explanation: 
# The numbers at indices 0 and 1 (2 and 7) add up to 9.    `]))
