def fun(nums):
    n=len(nums)


    nums[:]=[nums[n-1]]+nums[0:n-1]
    return nums
  
nums=[1,2,5,6,7,8,4]
print(f"{fun(nums)}")