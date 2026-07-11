def fun (nums,target=3):
    n=len(nums)
    low=0
    high=n-1
    ud=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ud=mid
            high=mid-1
        else:
            low=mid+1
    return ud
                