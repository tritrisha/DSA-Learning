class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combo(x, t, l, p):
            if t==0 and l==0:
                res.append(p[:])
                return 
            if x>=10:
                return 
            for i in range(x, 10):
                if i<=t:
                    p.append(i)
                    combo(i+1, t-i, l-1, p)
                    p.pop()

        res=[]
        combo(1, n, k, [])
        return res
        