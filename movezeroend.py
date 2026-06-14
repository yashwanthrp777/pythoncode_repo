nums=[1,0,2,3,4,5,8,0,5]
n=len(nums)
temp=[ ]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])

n2=len(temp)
for i in range(0,n2):
    temp[i]=nums[i]
for i in range(n,n2):
        nums[i]=0
print(temp)        

        


