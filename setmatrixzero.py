def funct(nums, row, col):
    r = len(nums)
    c = len(nums[0])

    # Mark the column
    for i in range(r):
        if nums[i][col] != 0:
            nums[i][col] = float("inf")

    # Mark the row
    for j in range(c):
        if nums[row][j] != 0:
            nums[row][j] = float("inf")


def setzero(nums):
    r = len(nums)
    c = len(nums[0])

    for i in range(r):
        for j in range(c):
            if nums[i][j] == 0:
                funct(nums, i, j)

    for i in range(r):
        for j in range(c):
            if nums[i][j] == float("inf"):
                nums[i][j] = 0

    return nums


nums = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

print(setzero(nums))