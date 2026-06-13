def rotate(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
    return nums
nums=[1,4,2,5,6,3,2]
print(f"{rotate(nums)} the rotata the value ")        