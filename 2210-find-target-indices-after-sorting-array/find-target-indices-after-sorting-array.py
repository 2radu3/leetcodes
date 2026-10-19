class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        nums.sort()

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        res = []
        while left < len(nums) and nums[left] == target:
            res.append(left)
            left += 1

        return res