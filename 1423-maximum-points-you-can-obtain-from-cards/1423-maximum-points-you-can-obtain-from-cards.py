class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=sum(cardPoints[:k])
        r=0
        maxs=l

        for i in range(k):
            l-=cardPoints[k-1-i]
            r+=cardPoints[len(cardPoints)-i-1]
            maxs=max(maxs, l+r)

        return maxs


        
        




            


        


            






        

            



            
        

        
        