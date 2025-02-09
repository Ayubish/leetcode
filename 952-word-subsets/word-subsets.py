class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans=[]
        wrd2=Counter()
        for x in words2:
            wrd2=wrd2 | Counter(x)
        for word in words1:
            wrd=Counter(word)
            flag=1
            for i in wrd2:
                if wrd2[i]>wrd[i]:
                    flag=0
                    break
            if (flag):
                ans.append(word)
            
        return ans

                