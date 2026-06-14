nums=[3,5,7,1,9,8]
k=3
n=len(nums)
result=k%n


for  _  in range(0,result):
    e=nums.pop()
    nums.insert(0,e)
print(nums)
print(result)
print(n)