def largest(nums):
    largest_nums=nums[0]
    n=len(nums)
    for i in range(0,n):
        if nums[i]>largest_nums:
            largest_nums=nums[i]
    return largest_nums
nums=[9,34,56,22,77,88,44]
print(f"{largest(nums)}")   
