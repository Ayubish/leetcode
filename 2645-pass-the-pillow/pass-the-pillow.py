class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current = 1
        forward = True
        for i in range(time):
            if current == n:
                forward = False
            elif current == 1:
                forward = True
            if forward:
                current += 1
            else: 
                current -= 1
        return current