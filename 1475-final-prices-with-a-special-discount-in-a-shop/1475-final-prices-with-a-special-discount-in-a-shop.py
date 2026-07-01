class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new=[]
        for i in range(len(prices)-1):
            j=i+1
            while prices[i]<prices[j]:
                if j<len(prices)-1:
                    j+=1
                else:
                    break
            if prices[i]>=prices[j]:
                new.append(prices[i]-prices[j])
            else:
                new.append(prices[i])


        new.append(prices[-1])
        return new




            






        

        
        