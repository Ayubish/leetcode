class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for dom in paths:
            splitted = dom.split()
            for i in range(1, len(splitted)):
                sub = splitted[i].split("(")
                dicto[sub[1][:-1]].append('/'.join([splitted[0], sub[0]]))
        ans = [item for item in dicto.values() if len(item)>1]
        return ans