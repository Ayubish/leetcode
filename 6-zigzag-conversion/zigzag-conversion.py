class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        t = [[None]*numRows for _ in range(n)]
        row = 0
        col = 0
        zig = numRows-2
        for i in range(n):
            if col == numRows:
                row += 1
                if zig > 0:
                    t[row][zig]=s[i]
                    zig -= 1
                    continue
                else:
                    zig = numRows-2
                    col = 0
            t[row][col] = s[i]
            col+=1
        newS = ""
        for x in range(numRows):
            for y in range(len(t)):
                if t[y][x]:
                    newS+= t[y][x]
        return newS