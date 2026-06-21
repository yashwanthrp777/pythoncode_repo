def funct(nums):
    n=len(nums)
    min_price=float("inf")
    max_price=0
    for i in range(0,n):
        min_price=min(min_price,nums[i])
        max_price=max(max_price,nums[i]-min_price)
    return max_price
nums=[2,3,1,4,5,6,7,8]
print(f"{funct(nums)}")    