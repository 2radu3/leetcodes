class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        max_length = 0
        for num in counts:
            if num + 1 in counts: 
                current_length = counts[num] + counts[num + 1] # How many times does num appears
                if current_length > max_length:
                    max_length = current_length

        return max_length