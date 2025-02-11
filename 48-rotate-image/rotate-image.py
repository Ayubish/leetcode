class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        top = 0
        bottom = len(matrix)-1
        while top < bottom:
            for col in range(len(matrix)):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(len(matrix)):
            for col in range(row+1, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix