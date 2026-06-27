class Solution:
    def isHappy(self, n: int) -> bool:
        k=str(n)
        print(k)
        r=20
        def repeat(kk: str):
            p=0
            for i in kk:
                p = p + (int(i)*int(i))

            return p

        while r:
            
            if repeat(k)==1:
                return True

            else:
                k=str(repeat(k))
            r-=1

        return False



            

        