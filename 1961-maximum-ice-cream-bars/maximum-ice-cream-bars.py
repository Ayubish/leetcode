class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = [0]*(max(costs)+1)
        count = 0
        spent = 0
        for cost in costs:
            arr[cost] += 1
        for i in range(len(arr)):
            for j in range(arr[i]):
                if spent+i<=coins:
                    count += 1
                    spent += i
                else:
                    return count
        return count
             

        