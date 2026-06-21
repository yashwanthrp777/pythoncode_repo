def funct(nums):
    maxi=float("-inf")
    for i in range(0,len(nums)):
        total=0
        for j in range(0,len(nums)):
            total=total+nums[i]
            maxi=max(maxi,total)
    return maxi
nums=[-1,2,-3,4,-1,5,6,7,-4,3]        
print(f"{funct(nums)}")

