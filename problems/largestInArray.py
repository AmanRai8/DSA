class Solution:
    def findLargest(self, nums: list[int]) -> int:
        largest = nums[0]  
        
        for n in nums:
            if n > largest:
                largest = n
        
        return largest
