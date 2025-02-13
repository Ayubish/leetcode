class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = []
        n = len(skill)
        skillcap = skill[0]+skill[-1]
        chemistry = 0
        for i in range(n//2):
            pair = [skill[i], skill[n-1-i]]
            if sum(pair)==skillcap:
                chemistry += pair[0]*pair[1]
            else:
                return -1
        return chemistry