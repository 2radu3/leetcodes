class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total, leftSum = sum(nums), 0
        for i, num in enumerate(nums):
            rightSum = total - leftSum - num
            if rightSum == leftSum:
                return i
            leftSum += num
        return -1
            
