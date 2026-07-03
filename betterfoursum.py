nums=[1,-1,0,-2,2,-1,3,5,4]
n=len(nums)
target=0
set_num=set()
for i in range(0,n):
    for j in range(i+1,n):
        hash_set=set()
        for k in range(j+1,n):
            forth=target-(nums[i]+nums[j]+nums[k])
            if forth in hash_set:
                temp=[nums[i],nums[j],nums[k],forth]
                temp.sort()
                set_num.add(tuple(temp))
            hash_set.add(nums[k])
result=[]
for ans in set_num:
    result.append(list(ans))
    print(result)


