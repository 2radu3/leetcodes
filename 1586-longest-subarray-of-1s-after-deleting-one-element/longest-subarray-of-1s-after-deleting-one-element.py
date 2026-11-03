class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_w = 0
        n = len(nums)
        l = 0
        num_zeros = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            w = r - l
            max_w = max(max_w, w)
        return max_w

