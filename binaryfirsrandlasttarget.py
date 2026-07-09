nums=[1,2,2,3,4,4,5,6,7,8,9]
target=4
first=-1
last=-1
n=len(nums)
for i in range(0,n):
    if nums[i]==target:
        if first==-1:
            first=i
        last=i
print(f"first={first} last={last}")

