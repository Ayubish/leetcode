class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBox1 = set()
        subBox2 = set()
        subBox3 = set()
        for i in range(9):
            rowSet = set()
            colSet = set()

            if i == 3 or i == 6:
                subBox1 = set()
                subBox2 = set()
                subBox3 = set()
            for j in range(9):
                num = board[i][j]
                if num != "." and num in rowSet:
                    return False
                else:
                    rowSet.add(num)

                num = board[j][i]
                if num != "." and num in colSet:
                    return False
                else:
                    colSet.add(num)
                if j<3:
                    if board[i][j] != "." and board[i][j] in subBox1:
                        return False
                    else:
                        subBox1.add(board[i][j])
                elif j<6:
                    if board[i][j] != "." and board[i][j] in subBox2:
                        return False
                    else:
                        subBox2.add(board[i][j])
                else:
                    if board[i][j] != "." and board[i][j] in subBox3:
                        return False
                    else:
                        subBox3.add(board[i][j])
        else:
            return True
                
                