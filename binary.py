def binary_search(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
nums=[1,3,4,5,6,8,9,10]
target=5
result=binary_search(nums,target)
if result!=-1:
    print(f"element found at index {result}")
else:
    print("element not found in the list")
        