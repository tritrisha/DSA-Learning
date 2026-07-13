class Solution:
    def fillCups(self, amount: List[int]) -> int:
        n=0
        if len(amount)==amount.count(0):
            return 0

        while len(amount)!=amount.count(0):
            amount.sort()
            while amount[0]==0:
                amount.pop(0)
            if amount:
                if len(amount)!=1:
                    amount[0]-=1
                    amount[-1]-=1
                else:
                    amount[0]-=1
            else:
                break
            n+=1
            
        return n




            

        