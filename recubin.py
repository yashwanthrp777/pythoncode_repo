def fun(nums,low,high):
    mid=(low+high)//2
    if low>high:
        return -1
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return fun(nums,mid+1,high)
    else:
        return fun(nums,low,mid-1)
target=int(input("enter the target:  "))
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
print(fun(nums,0,len(nums)-1))
