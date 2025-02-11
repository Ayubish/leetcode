class Solution:
    def frequencySort(self, s: str) -> str:
        dicto = Counter(s)
        final = []
        for key, val in dicto.items():
            final.append([key, val])
        final.sort(key= lambda item: item[1], reverse=True)
        superfinal = [k[1]*k[0] for k in final]
        return "".join(superfinal)
       