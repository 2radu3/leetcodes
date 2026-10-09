class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        index = 0
        for i in range(len(nums)):
            sumLeft, sumRight = sum(nums[:i]), sum(nums[i + 1:])
            if sumLeft == sumRight:
                return i
            
        return -1
            
