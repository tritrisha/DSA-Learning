class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        h={}
        for i in range(len(edges)):
            if edges[i] in h:
                h[edges[i]]+=i

            else:
                h[edges[i]]=i

        m=0
        mi=0
        for i in h:
            if mi<h[i]:
                m=i
                mi=h[i]

            elif mi==h[i]:
                m=min(m, i)

        return m


        