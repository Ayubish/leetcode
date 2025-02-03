class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        answer = [[],[]]
        for arr in matches:
            if arr[0] in winners:
                winners[arr[0]] += 1
            else:
                winners[arr[0]]= 1
            if arr[1] in losers:
                losers[arr[1]] += 1
            else:
                losers[arr[1]]= 1
        for item in losers:
            if losers[item] == 1:
                answer[1].append(item)
        for item in winners:
            if item not in losers:
                answer[0].append(item)
        answer[0].sort()
        answer[1].sort()
        return answer