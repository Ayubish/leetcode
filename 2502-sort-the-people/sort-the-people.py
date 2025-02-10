class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxi = max(heights)
        history = [0 for _ in range(maxi+1)]
        for i in range(len(names)):
            history[heights[i]] = names[i]
        history = history[::-1]
        names = [name for name in history if name!=0]
        return names