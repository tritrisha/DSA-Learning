class ProductOfNumbers:

    def __init__(self):
        self.pon=[]

    def add(self, num: int) -> None:
        self.pon.append(num)

    def getProduct(self, k: int) -> int:
        n=len(self.pon)
        return prod(self.pon[n-k:n+1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)