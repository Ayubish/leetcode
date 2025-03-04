class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        return "1"*(count["1"]-1) + "0"*count["0"] + "1"