class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        min = 0
        for i in range(len(names)):
            for j in range(i, len(names)):
                if heights[j]>heights[min]: 
                    heights[j], heights[min] = heights[min], heights[j]
                    names[j], names[min] = names[min], names[j]
            min += 1
        return names