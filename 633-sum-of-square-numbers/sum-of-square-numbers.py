class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = 0
        y = int(c**0.5)
        while x<=y:
            n = x*x + y*y
            if n==c:
                return True
            elif n>c:
                y -= 1
            else:
                x += 1
        return False