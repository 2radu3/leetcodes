class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sum += nums[i]
            else:
                break
        while sum in num_set:
            sum += 1
        return sum