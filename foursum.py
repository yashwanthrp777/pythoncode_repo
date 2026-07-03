nums=[1,-1,0,0,1,2,-2,4,5]
n=len(nums)
my_set=set()
if n<4:
    print([])
else:

    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==0:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
result=[]
for avs in my_set:
    result.append(list(avs))
    print(result)


