class Solution:
    def reverseArray(self, nums: list[int]) -> None:
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]  # swap
            left += 1
            right -= 1
        print(nums)