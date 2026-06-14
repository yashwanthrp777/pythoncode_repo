nums=[2,3,5,7,6,8,9]
print(nums)
n=len(nums)
k=5
result=k%n
nums[:]=nums[n-k:]+nums[:n-k]
print(nums)

