def arr_sort(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=[34,56,12,98,99]
print(f"{arr_sort(nums)} arr is sorted")
