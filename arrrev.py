def fun(nums, left, right):

    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]

    fun(nums, left + 1, right - 1)


def reverseArray(nums):
    fun(nums, 0, len(nums) - 1)
    return nums


print(reverseArray([1,2,3,4,5]))