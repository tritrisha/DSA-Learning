class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        m1=None
        m2=None
        for i in nums:
            if m1==i:
                c1+=1
            elif m2==i:
                c2+=1
            elif c1==0:
                m1=i
                c1+=1
            elif c2==0:
                m2=i
                c2+=1
            else:
                c1-=1
                c2-=1

        c1, c2=0,0
        for i in nums:
            if i==m1:
                c1+=1

            if i==m2:
                c2+=1

        res=[]
        if c1>len(nums)//3:
            res.append(m1)

        if c2>len(nums)//3:
            res.append(m2)

        return res



            


        