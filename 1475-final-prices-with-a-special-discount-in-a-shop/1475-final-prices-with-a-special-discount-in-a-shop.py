class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        j=1
        new=[]
        for i in range(len(prices)-1):
            

            if prices[j]<=prices[i]:
                new.append(prices[i]-prices[j])

            else:
                k=j
                while prices[k]>prices[i]:
                    if k<len(prices)-1:
                        k+=1
                    else:
                        break
                if prices[k]<=prices[i]:  
                    new.append(prices[i]-prices[k])
                else:
                    new.append(prices[i])


            if j<len(prices)-1:
                j+=1

            
        new.append(prices[-1])

        return new


        






        
        