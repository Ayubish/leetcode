class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        ans = [matrix[i][j]]
        cursor = (0, 1)
        direction = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        matrix[i][j] = None
        while len(ans)<m*n:
            row = i + cursor[0]
            col = j + cursor[1]
            if (row < 0 or row == n 
            or col < 0 or col == m 
            or matrix[row][col] is None):
                cursor = direction[cursor]
            else:
                i, j = row, col
                ans.append(matrix[i][j])
                matrix[i][j] = None
        return ans
