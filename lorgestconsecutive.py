def fun(nums):
    max_count=0
    n=len(nums)
    for i in range(0,n):
        num=nums[i]
        count=0
        while num+1 in nums:
            count+=1
            num=num+1
            max_count=max(max_count,count)
    return max_count
nums=[1,4,2,3,5,4,44,66,88]

print(fun(nums))
