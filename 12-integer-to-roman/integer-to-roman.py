class Solution:
    def intToRoman(self, num: int) -> str:
        dic = [
        ['I','II','III','IV','V','VI','VII','VIII','IX'],
        ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        ['M','MM','MMM']
        ]
        num = str(num)
        n = len(num)
        roman = ""
        for i in range(n):
            if int(num[i])==0:
                continue
            j = n-i
            k = int(num[i])
            roman +=  dic[j-1][k-1]
        return roman
