class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(len(names)):
                if heights[i]>heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        return names