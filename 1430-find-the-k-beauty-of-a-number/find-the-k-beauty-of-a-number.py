class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        L = 0
        R = k
        str_num = str(num)
        count = 0
        while R <= len(str_num):
            res = int(str_num[L:R])
            L += 1
            R += 1
            if res == 0:
                continue
            if num % res == 0:
                count += 1
            
        return count
