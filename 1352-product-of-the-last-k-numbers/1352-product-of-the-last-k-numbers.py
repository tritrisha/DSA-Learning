class ProductOfNumbers:

    def __init__(self):
        self.pon=[1]

    def add(self, num: int) -> None:
        if num==0:
            self.pon=[1]
        else:
            self.pon.append(self.pon[-1] * num)

    def getProduct(self, k: int) -> int:
        if k>=len(self.pon):
            return 0

        return self.pon[-1]//self.pon[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)