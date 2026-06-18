def funct(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
nums=[0,1,3,4,5,6,7]    
print(f"{funct(nums)}")