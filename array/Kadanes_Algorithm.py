#Kadane’s Algorithm (Maximum Subarray Sum)


def max_subarray(nums):
    max_ending_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far,max_ending_here)
    return max_so_far

nums= [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6