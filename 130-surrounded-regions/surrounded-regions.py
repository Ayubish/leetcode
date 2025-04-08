class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(row, col):
            print(row, col)
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == "X":
                return
            if board[row][col] == "O":
                board[row][col] = "S"
            else:
                return
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if (row == rows-1 or row == 0 or col == cols-1 or col == 0) and board[row][col] == "O":
                    dfs(row, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
            

        