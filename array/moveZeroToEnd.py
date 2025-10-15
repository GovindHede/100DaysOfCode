def move_zeros(nums):
    pos = 0
    for num in nums:
        if num !=0:
            nums[pos] = num
            pos +=1
    while pos < len(nums):
        nums[pos] =0
        pos +=1
    return nums
nums = [0,1,0,3,12]
print(move_zeros(nums))  # Output: [1, 3, 12, 0, 0]