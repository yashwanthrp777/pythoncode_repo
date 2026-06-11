def second(nums):
    largest=float("-inf")
    second_larg=float("-inf")
    n=len(nums)
    for i in range(0,n):
        if nums[i]>largest:
         second_larg=largest
         largest=nums[i]
        elif nums[i]>second_larg and nums[i]!= largest:
           second_larg=nums[i]
    return second_larg
nums=[33,55,77,22,12,88,99]        
  

print( f"{second(nums)}  is the second largest number")
        
        

