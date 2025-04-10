class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winners = set([i for i in range(n)])

        for a, b in edges:
            if b in winners:
                winners.remove(b)
        if len(winners) > 1:
            return -1
        return list(winners)[0]