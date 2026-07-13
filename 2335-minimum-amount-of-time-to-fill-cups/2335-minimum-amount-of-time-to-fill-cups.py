class Solution:
    def fillCups(self, amount: List[int]) -> int:
        r=[]
        for i in amount:
            r.append(i)
        r.sort()
        n=0
        if len(r)==r.count(0):
            return 0
        while len(r)!=r.count(0):
            print(r)
            while r[0]==0:
                r.pop(0)
            if r:
                if len(r)!=1:
                    r[0]=r[0]-1
                    r[-1]=r[-1]-1
                else:
                    r[0]=r[0]-1

            else:
                break

            n+=1
            r.sort()

        return n




            

        