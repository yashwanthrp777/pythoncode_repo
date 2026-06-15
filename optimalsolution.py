def funct(nums):
    i = 0  

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

nums = [1, 0, 3, 5, 4, 0, 0, 6, 5]
print(funct(nums))