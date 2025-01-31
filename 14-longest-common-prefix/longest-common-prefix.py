class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        strs.sort()
        first = strs[0]
        for i in range(len(first)):
            for k in range(1, len(strs)):
                if first[i] != strs[k][i]:
                    return common
            common += first[i]
        return common