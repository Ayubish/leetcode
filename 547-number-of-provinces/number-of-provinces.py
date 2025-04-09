class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        total = 0

        def dfs(node):
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1 and i not in visited:
                    dfs(i)

        for i in range(n):
            if i not in visited:
                total += 1
                dfs(i)
        return total