class Solution:
    def getLucky(self, s: str, k: int) -> int:
        inti = ""
        for char in s:
            inti += str(ord(char)-96)
        for _ in range(k):
            for char in inti:
                sumi = sum([int(k) for k in inti])
            inti = str(sumi)
        return int(inti)
