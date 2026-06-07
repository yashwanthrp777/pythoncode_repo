def swap(left,right,nums):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    swap(left+1,right-1,nums)
nums=[3,4,2,5,6,7,8,5,6]
swap(0,len(nums)-1,nums)
print(nums)
        
