class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            if b==0:
                return a
            else:
                return gcd(b, a%b)
           
        x=0
        g=[]
        for i in range(len(nums)):
            x=max(x, nums[i])
            g.append(gcd(nums[i], x))


        g.sort()
        r=0
        l=0
        p=len(g)-1
        print(g)
        while l<p:
            print(gcd(g[l], g[p]))
            r+=gcd(g[l], g[p])
            l+=1
            p-=1
        return r


        




        