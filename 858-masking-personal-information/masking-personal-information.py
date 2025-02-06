class Solution:
    def maskEmail(self, s):
        splitted = s.split("@")
        return splitted[0][0].lower() + "*****" + splitted[0][-1].lower() + "@" + splitted[1].lower()
    def maskPhone(self, s):
        phone = ""
        for char in s:
            if char.isalnum():
                phone += char
        if len(phone)==10:
            return "***-***-"+phone[-4:len(s)]
        elif len(phone)==11:
            return "+*-***-***-"+phone[-4:len(s)]
        elif len(phone)==12:
            return "+**-***-***-"+phone[-4:len(s)]
        else:
            return "+***-***-***-"+phone[-4:len(s)]
    def maskPII(self, s: str) -> str:
        if "@" in set(s):
            return self.maskEmail(s)
        else:
            return self.maskPhone(s)
        