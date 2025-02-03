from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicto = defaultdict(int)
        dicta = defaultdict(int)
        for chars in s:
            dicto[chars] += 1
        for chars in t:
            dicta[chars] += 1
        if dicto == dicta:
            return True
        else:
            return False