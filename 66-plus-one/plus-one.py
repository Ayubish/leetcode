class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        return [int(k) for k in list(str(int(s)+1))]