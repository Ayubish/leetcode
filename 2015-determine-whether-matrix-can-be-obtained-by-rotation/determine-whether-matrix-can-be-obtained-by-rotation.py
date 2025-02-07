class Solution:
    def transpose(self, matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(5):
            if mat == target:
                return True
            target = self.transpose(target[::-1])
        else:
            return False