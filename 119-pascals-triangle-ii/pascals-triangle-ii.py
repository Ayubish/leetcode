class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        while len(ans) <= rowIndex:
            tmp = []
            for i in range(len(ans)-1):
                tmp.append(ans[i] + ans[i+1])
            ans = [1] + tmp + [1]
        return ans