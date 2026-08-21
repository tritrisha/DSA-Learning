class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        s = []
        def ds(t, i, s, p):
            if i>=n:
                return 
            if t==0:
                s.append(p[:])
                return 

            if t>=candidates[i]:
                p.append(candidates[i])
                ds(t-candidates[i], i, s, p)
                p.pop() 
            ds(t, i+1, s, p)


        ds(target,0, s, [])
        return s