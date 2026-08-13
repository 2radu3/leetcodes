class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n in memo: return memo[n]
        if n == 0: return 0
        if n <= 2: return 1
        memo[n] = self.fib(n - 2) + self.fib(n - 1)
        return memo[n]
        