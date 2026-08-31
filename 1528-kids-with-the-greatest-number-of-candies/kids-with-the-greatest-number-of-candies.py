class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        Max = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= Max:
                res[i] = True
        return res