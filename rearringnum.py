def fun(nums):
    pos=[ ]
    neg=[ ]

    for num in nums:
        if num>0:
            pos.append(num)
        else:
            neg.append(num)
    result=[0]*len(nums)        

    for i in range(0,len(pos)):
        result[2*i]=pos[i]
        result[2*i+1]=neg[i]
    return result
nums=[1,3,-2,5,-6,-4]
print(f"{fun(nums)}")     