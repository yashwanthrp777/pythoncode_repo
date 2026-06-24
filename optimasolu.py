def fun(nums):
    nums.sort()

    longest = 1
    count = 1

    for i in range(1, len(nums)):

        if nums[i] == nums[i-1] + 1:
            count += 1

        elif nums[i] != nums[i-1]:
            count = 1

        longest = max(longest, count)

    return longest


nums = [1,1,1,4,2,3,5,66,55,88]
print(fun(nums))