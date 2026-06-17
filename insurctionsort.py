def funct(nums):
    n=len(nums)
    
    if nums==1:
        return 1
    for i in range(n):
        if nums[i]==target:
            return i
nums=[2,3,5,7,8,95]
target=2
print(f"{funct(nums)}")


