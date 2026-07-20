class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for i in range(k):
            last_val = grid[m - 1][n - 1]

            for r in range(m - 1, -1, -1):
                for c in range(n - 1, -1, -1):
                    if c == 0:
                        if r > 0:
                            grid[r][c] = grid[r - 1][n - 1]
                    else:
                        grid[r][c] = grid[r][c - 1]
            grid[0][0] = last_val

        return grid