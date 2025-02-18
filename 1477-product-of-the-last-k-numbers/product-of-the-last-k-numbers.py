class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.var = 1
    def add(self, num: int) -> None:
        if num==0:
            self.nums = [0]*(len(self.nums)+1)
            self.var = 1
        else:
            self.var *= num
            self.nums.append(self.var)

    def getProduct(self, k: int) -> int:
        if self.nums[-k] == 0:
            return 0
        elif len(self.nums)-k<1:
            return self.nums[-1]
        elif self.nums[-k-1] == 0:
            return self.nums[-1]
        return self.nums[-1]//self.nums[-k-1]
        
        
        
        
        # prod = 1
        # for i in range(1, k+1):
        #     prod *= self.nums[-i]

        # return prod

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)