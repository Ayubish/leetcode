class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        n = len(piles)
        good_piles = piles[n//3:]
        for i in range(0, len(good_piles), 2):
            sum += good_piles[i]
        return sum
