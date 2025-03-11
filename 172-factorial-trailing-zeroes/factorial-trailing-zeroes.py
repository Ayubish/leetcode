class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(100000)
        def fac(n):
            if n == 0:
                return 1
            return n*fac(n-1)
        s = str(fac(n))
        count = 0
        i = len(s)-1
        while i>0 and s[i] == "0":
            count += 1
            i -= 1
        return count
            