class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        multiComment = False
        ans = []
        nonComment = ""    #"struct Nod"
        for line in source: #["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
            i=0
            while i<len(line):
                if i+1<len(line) and line[i]=="/" and line[i+1]=="*" and not multiComment:
                    multiComment = True
                    i+=2
                    continue
                elif i+1<len(line) and line[i]=="/" and line[i+1]=="/" and not multiComment:
                    if len(nonComment)>0:
                        ans.append(nonComment)
                        nonComment=""
                    break
                    
                elif i+1<len(line) and line[i]=="*" and line[i+1]=="/" and multiComment:
                    multiComment = False
                    i+=2
                    continue
                else:
                    if not multiComment:
                        nonComment += line[i]
                    i+=1
            if len(nonComment)>0 and not multiComment:
                ans.append(nonComment)
                nonComment=""

        return ans
            
                    