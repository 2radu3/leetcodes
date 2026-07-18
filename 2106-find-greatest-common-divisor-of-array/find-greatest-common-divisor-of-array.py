class Solution:
    def findGCD(self, nums: List[int]) -> int:
        Max = max(nums)
        Min = min (nums)

        while Min != 0:
            r = Max % Min
            Max = Min
            Min = r
        return Max