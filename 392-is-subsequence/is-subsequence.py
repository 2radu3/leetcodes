class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        count = 0
        if len(s) < 1:
            return True

        for x in t:
            if x == s[ps]:
                ps += 1
                count += 1
            if count == len(s):
                return True
        return False