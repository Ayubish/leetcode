class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        my_drink = numBottles
        ratio = numBottles//numExchange
        my_drink += ratio
        carry = ratio + numBottles%numExchange
        while carry>=numExchange:
            ratio = carry//numExchange
            my_drink += ratio
            carry = ratio + carry%numExchange
        return my_drink