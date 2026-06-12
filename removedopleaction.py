def rev(nums):
    n=len(nums)
    frac_num={}
    for i in range(0,n):
        frac_num[nums[i]]=0
    j=0

    for key in frac_num:
        nums[j]=key
        j+=1
    return j
nums=[1,1,1,2,2,3,3,4,5,6,7,8,8,8,9] 
print(f"{rev(nums)} sotrd numbers ")

