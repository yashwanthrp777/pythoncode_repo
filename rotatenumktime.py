nums=[2,4,3,5,6,7]
k=3
n=len(nums)
rotate=k%n
for _ in range(0,rotate):
    e=nums.pop()
    nums.insert(0,k)