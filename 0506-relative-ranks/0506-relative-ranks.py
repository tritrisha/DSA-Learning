class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        r=[]
        for i, s in enumerate(score):
            heappush(r, [-s,i])
        
        k=[""]*len(score)
        n=len(r)
        for i in range(n):
            x=r[0][1]
            if i==0:
                k[x]="Gold Medal"

            elif i==1:
                k[x]="Silver Medal"

            elif i==2:
                k[x]="Bronze Medal"

            else:
                k[x]=str(i+1)

            r.pop(0)
            heapify(r)

        return k

            







        

        
        