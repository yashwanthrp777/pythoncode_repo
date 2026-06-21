def funct(nums):
    max_price=0
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                price=nums[j]-nums[i]
                max_price=max(max_price,price)
    return max_price
nums=[2,1,5,4,8,5,9]
print(f"{funct(nums)}")            