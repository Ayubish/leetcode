class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dicto = defaultdict(int)
        ans = []
        set1 = set(list1)
        set2 = set(list2)
        for i in range(len(list1)):
            if list1[i] in set1 and list1[i] in set2:
                dicto[list1[i]] += i
        for i in range(len(list2)):
            if list2[i] in dicto:
                dicto[list2[i]] += i
        mini = min(list(dicto.values()))
        for item in dicto:
            if dicto[item] == mini:
                ans.append(item)
        return ans