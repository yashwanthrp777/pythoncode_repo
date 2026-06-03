def insert(nums):
    n=len(nums)
    for i in range(1,n):
        j=i-1
        key=nums[i]
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
            nums[j+1]=key
    return nums
nums=[44,33,55,22,5,6,5,1]        
print(insert(nums))