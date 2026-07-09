def fun(nums):
    cile=-1
    floow=-1
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low +high)//2
        if nums[mid]==target:
            return[nums[mid],nums[mid]]
        elif nums[mid]<target:
                  floow=nums[mid]
                  low=mid+1
        else:
                  cile=nums[mid]
                  high=mid-1
 
    return [floow,cile]
target=3
nums=[1,2,2,4,4,5,6,7,8,9] 
print(fun(nums))                       
                  
