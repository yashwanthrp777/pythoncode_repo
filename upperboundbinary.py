def fun (nums):
    n=len(nums)
    u_b=n
    low =0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            low=mid+1
            u_b=mid
        else:
            high=mid-1
    return u_b
nums=[1,1,1,2,2,2,3,3,4,4,4,5,6,6,7,8,9]
target=4
print(fun(nums))
