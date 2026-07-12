def fun(nums):
    n=len(nums)
    min_val=float('inf')
    for i in range(0,n):
        min_val=min(min_val,nums[i])
    return min_val
nums=[11,12,13,1,2,3,4,0,5,6,-1]
print(fun(nums))
