class Solution:
    def getLucky(self, s: str, k: int) -> int:
        inti = ''.join([str(ord(char)-96) for char in s])
        for _ in range(k):
            sumi = sum([int(k) for k in inti])
            inti = str(sumi)
        return int(inti)
