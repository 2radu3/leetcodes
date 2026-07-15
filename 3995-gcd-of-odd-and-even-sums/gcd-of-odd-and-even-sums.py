class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        r = 0
        for i in range(2 * n):
            if (i % 2 == 0):
                sumEven += i
            else:
                sumOdd += i

        if (sumEven == 0):
            return 1
            
        r = sumEven % sumOdd
        while(sumOdd % r != 0):
            r = sumOdd % r
        
        return r

        
        