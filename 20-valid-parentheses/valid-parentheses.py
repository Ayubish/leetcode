class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in brackets:
                if not stack:
                    return False
                if brackets[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return True if not stack else False