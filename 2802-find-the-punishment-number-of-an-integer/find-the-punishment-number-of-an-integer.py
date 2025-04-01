class Solution:
    def punishmentNumber(self, n: int) -> int:
            
        def backtrack(num, square, i):
            if num in used:
                return
            number = str(num**2)
            if num == square and i == len(number):
                ans.append(num**2)
                used.add(num)
                return
            if num < (square) or i == len(number):
                return
            for j in range(i, len(number)):
                backtrack(num, square+int(number[i:j+1]), j+1)
            
            
        ans = []
        for i in range(1, n+1):
            num = str(i*i)
            used = set()
            for j, digit in enumerate(num):
                backtrack(i, int(num[:j+1]), j+1)

        return sum(ans)