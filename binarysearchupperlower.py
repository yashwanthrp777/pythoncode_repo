def fun(nums):
    n=len(nums)
    target=1
    low_b=-1
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
          low_b=mid
          high=mid-1
        else:
          low=mid+1
    return low_b
nums=[1,1,1,2,2,2,3,3,3,4,4,4,5,6,6,7,7,8,8,9]       
print(f"{fun(nums)}")


