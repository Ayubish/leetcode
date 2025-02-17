class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for left,right,step in shifts:
            if step==1:
                arr[left] += 1
                arr[right+1] -= 1
            else:
                arr[left] -= 1
                arr[right+1] += 1
        prefix_sum = []
        sum_ = 0
        for i in range(len(arr)-1):
            sum_ += arr[i]
            prefix_sum.append(sum_)
        ans = ""
        for i in range(len(s)):
            idx = (ord(s[i])-97+prefix_sum[i])%26
            ans += chr(97+idx)
        return ans