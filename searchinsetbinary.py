def fun(nums):
    n=len(nums)
    high=n-1
    low=0
    ld=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=tarhet:
            ld=mid
            high=mid-1
        else:
            low=mid+1
    return ld
nums=[1,3,4,5,6,7,8,9]
tarhet=2
print(fun(nums))            