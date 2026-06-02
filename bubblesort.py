def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
nums=[55,33,76,87,4,7]
print(bubble_sort(nums))
