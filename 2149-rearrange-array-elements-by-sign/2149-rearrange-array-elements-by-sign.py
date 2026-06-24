class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            if i>0:
                pos.append(i)

        k=[]
        for i in range(len(pos)):
            k.append(pos[i])
            k.append(neg[i])

        return k


        