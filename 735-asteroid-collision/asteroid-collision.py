class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for elem in asteroids:
            while stack and elem < 0 and stack[-1] > 0:
                diff = elem + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    elem = 0
                    break
                elif diff == 0:
                    stack.pop()
                    elem = 0
                    break
            if elem != 0:
                stack.append(elem)

        return stack
