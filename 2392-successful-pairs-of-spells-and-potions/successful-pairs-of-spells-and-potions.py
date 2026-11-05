class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res = []
        for s in spells:
            idx = len(potions)
            l, r = 0, len(potions) - 1

            while l <= r:
                m = (r + l) // 2

                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1

            res.append(len(potions) - idx)
        return res

        