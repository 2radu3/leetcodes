class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        a = 0
        maxgain = 0
        for i in gain:
            a += i
            if a > maxgain:
                maxgain = a
        return maxgain