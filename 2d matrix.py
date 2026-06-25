def func(nums):
    rows=len(nums)
    colm=len(nums[0])
    for i in range (0,rows):
        for j in range(0,colm):
            print(nums[i][j],end=" ")
    print()
nums=[[2,3,4],[5,6,7],[10,3,5]]
print(func(nums))
            



