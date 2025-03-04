class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRow = []
        maxCol = []
        sumi = 0
        for i in range(len(grid)):
            currMaxCol = 0
            currMaxRow = 0
            for j in range(len(grid)):
                currMaxCol = max(currMaxCol, grid[i][j])
                currMaxRow = max(currMaxRow, grid[j][i])
            maxRow.append(currMaxRow)
            maxCol.append(currMaxCol)
        for i in range(len(grid)):
            for j in range(len(grid)):
                sumi += min(maxRow[j], maxCol[i]) - grid[i][j]
        return sumi