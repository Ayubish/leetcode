class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cut = len(people)
        for i in range(len(people)):
            if people[i]>limit:
                cut = poeple[i]
                break
        boatneeded = len(people[cut:])
        left = 0
        right = cut-1

        while left<=right:
            if limit-(people[right]+people[left])>=0:
                boatneeded+=1
                right-=1
                left+=1
            else:
                boatneeded+=1
                right-=1
        return boatneeded