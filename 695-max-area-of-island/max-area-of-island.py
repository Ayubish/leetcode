class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxi = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            return 1 + dfs(row, col-1) + dfs(row, col+1) + dfs(row-1, col) + dfs(row+1, col)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxi = max(maxi, area)
        return maxi