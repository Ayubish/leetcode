class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(heights)
        for i in range(len(heights)-1, -1, -1):
            tot = 0
            while stack:
                if stack[-1] < heights[i]:
                    stack.pop()
                    tot += 1
                else:
                    tot += 1
                    break
            ans[i] = tot
            stack.append(heights[i])
        return ans

            