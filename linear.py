def funct(nums):
    n=len(nums)

    for i in range(n):
        if nums[i]==target:
            return i
nums=[2,3,5,7,8,95]
target=95
print(f"{funct(nums)}")


