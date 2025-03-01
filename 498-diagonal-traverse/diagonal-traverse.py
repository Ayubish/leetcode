class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat[0])
        m = len(mat)
        up = True
        ans = []
        i = 0
        j = 0
        while len(ans)<n*m:
            if up:
                if i<0 or j==n:
                    if j==n:
                        j -= 1
                        i += 1
                    up = False
                    i += 1
                    continue
                ans.append(mat[i][j])
                i -= 1
                j += 1
            else:
                if j<0 or i==m:
                    if i==m:
                        i -= 1
                        j += 1
                    up = True
                    j += 1
                    continue
                ans.append(mat[i][j])
                i += 1
                j -= 1
        return ans
