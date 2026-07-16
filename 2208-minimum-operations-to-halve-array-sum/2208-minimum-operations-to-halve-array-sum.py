class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s=sum(nums)/2
        n=0
        a=[-i for i in nums]
        heapify(a)
        while s>0:
            mi=heappop(a)/2.0
            s=s+mi
            heappush(a, mi)
            n+=1

        return n

            
            
        


            

            

        