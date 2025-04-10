class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = defaultdict(set)
        ans = []
        for pair in edges:
            parents[pair[1]].add(pair[0])
        def dfs(node, fam):
            for par in parents[node]:
                if par not in fam:
                    fam.add(par)
                    dfs(par, fam)
            return
        for i in range(n):
            fam = set()
            dfs(i, fam)
            ans.append(sorted(list(fam)))
        return ans