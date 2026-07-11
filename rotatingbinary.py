def fun(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
nums=[11,12,14,1,2,2,3,4,7,8,9]    
target=4
print(fun(nums,target))