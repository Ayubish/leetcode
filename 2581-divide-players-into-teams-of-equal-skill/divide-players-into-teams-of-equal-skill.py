class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = []
        n = len(skill)
        skillcap = skill[0]+skill[-1]
        for i in range(n//2):
            pair = [skill[i], skill[n-1-i]]
            if sum(pair)==skillcap:
                teams.append(pair)
            else:
                return -1
        teams = [a[0]*a[1] for a in teams]
        return sum(teams)