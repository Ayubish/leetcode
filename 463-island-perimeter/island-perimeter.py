class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1
            if grid[row][col] == -1:
                return 0
            grid[row][col] = -1

            return dfs(row - 1, col) + dfs(row, col - 1) + dfs(row + 1, col) + dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)
        return perimeter
