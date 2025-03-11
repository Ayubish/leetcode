class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        i = len(temperatures)-1

        
        while i>-1:
            if not stack:
                ans[i] = 0
                stack.append(i)
            elif temperatures[i]>=temperatures[stack[-1]]:
                while stack and temperatures[i]>=temperatures[stack[-1]]:
                    stack.pop()
                continue
            else:
                ans[i] = stack[-1] - i
                stack.append(i)
            i-=1
        return ans