class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        if count_s1 == count_s2:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            count_s2[s2[left]]-=1
            if not count_s2[s2[left]]:
                count_s2.pop(s2[left])
            count_s2[s2[right]]+=1
            if count_s1 == count_s2:
                return True
            left += 1
        return False

        