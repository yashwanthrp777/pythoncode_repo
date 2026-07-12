def fun(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
        if nums[low]<=nums[mid]:    
            if nums[mid]<=target<nums[high]:
                high=mid-1
            else:
                low=mid+1
        else:        
            if nums[mid]<=target<nums[low]:
                    high=mid-1
            else:
                    low=mid+1
    return False
nums=[7,7,7,8,8,9,1,2,3,4,5,6,7]     
print(fun(nums,7))

