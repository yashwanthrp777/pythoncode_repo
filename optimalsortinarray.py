def arr(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i+=1
            nums[j],nums[i]=nums[i],nums[j]
        j+=1   
    return i+1
nums=[1,1,2,3,3,4,4,5,5,6,6,7,7]         
print(f"{arr(nums)} sorted array number")
