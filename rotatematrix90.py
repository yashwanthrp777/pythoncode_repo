def fun(nums):
    n=len(nums)
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result[j][(n-i)-1]=nums[i][j]
    return result
nums=[[1,3,2],[4,6,5],[7,6,5]]
print(fun(nums))
