class Solution:
    def decodeString(self, s: str) -> str:
        if s.isalpha():
            return s
        ans = ""
        i = 0
        while i < len(s):
            
            if s[i].isdigit():
                num = s[i]
                i += 1 
                while s[i].isdigit():
                    num += s[i]
                    i+=1
                
                left = i+1
                k = 1
                i += 1
                while k:
                    if s[i] == "[":
                        k+=1
                    elif s[i] == "]":
                        k -= 1
                    i+=1
                right =  i-1
                ans += int(num)*self.decodeString(s[left:right])
            else:
                ans += s[i]
                i+=1
        return ans