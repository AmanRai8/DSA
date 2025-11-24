class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        largest = second = float('-inf')  # initialize to negative infinity

        for num in nums:
            if num > largest:
                second = largest
                largest = num
            elif largest > num > second:  # only update second if it's less than largest but greater than current second
                second = num

        return second