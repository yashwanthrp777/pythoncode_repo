def twosum(nums):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
         if nums[i]+nums[j] == target:
         
           return [i,j]
    return nums
target=13
nums=[5,4,1,2,5,8]
print(f"{twosum(nums),(target)}")
