def revers(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

    revers(n-k,n-1)
    revers(0,n-k-1)
    revers(0,n-1)
k=5
nums=[2,4,3,5,6,7,8]
n=len(nums)

print(revers(nums)) 


