class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def com(t, i, s, p):
            if t==0:
                s.append(p[:])
                return 

            for x in range(i, n):
                if x>i and candidates[x]==candidates[x-1]:
                    continue
                if t<candidates[x]:
                    break
                if t>=candidates[x]:
                    p.append(candidates[x])
                    com(t-candidates[x], x+1, s, p)
                    p.pop()
                    
        s=[]
        n=len(candidates)
        com(target, 0, s, [])
        return s


        