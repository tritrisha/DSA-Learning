class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i=0
        n=0
        while tickets[k]!=0:
            if tickets[i]>0:
                tickets[i]-=1
                n+=1
            if i<len(tickets)-1:
                i+=1
            else:
                i=0

        return n


        

            
            

            

        






        