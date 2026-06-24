class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        m=0
        n=0
        for i in s:
            if i=="(":
                st.append(i)

            if i==")":
                n=len(st)
                st.pop()
            m=max(n, m)

        return m



        pri

                



        




        