class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        r=[]
        for i in range(1, n+1):
            r.append(str(i))

        r.sort()
        k=[]
        for i in r:
            k.append(int(i))

        return k
        







        