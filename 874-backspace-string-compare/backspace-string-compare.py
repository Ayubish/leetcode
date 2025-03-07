class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []
        for char in s:
            if char == "#":
                if stack_a:
                    stack_a.pop()
            else:
                stack_a.append(char)
        for char in t:
            if char == "#":
                if stack_b:
                    stack_b.pop()
            else:
                stack_b.append(char)
        return stack_a == stack_b
