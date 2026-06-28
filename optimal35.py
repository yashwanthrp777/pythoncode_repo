def fun(nums):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    return nums 
nums=[[2,4,3],[1,4,3],[5,7,6]] 
print(fun(nums))      