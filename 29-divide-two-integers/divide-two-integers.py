class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        co = dividend/divisor
        co = math.ceil(co) if co<0 else math.floor(co)
        if co > (2**31)-1:
            return (2**31)-1
        if co<(-2**31):
            return (-2**31)
        return co