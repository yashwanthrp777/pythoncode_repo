def fun(nums):
    n=len(nums)
    target=3
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
nums=[1,2,3,4,5,6,7,8,9,10]
print(f"{fun(nums)}")
