class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if not st:
                st.append(s[i])
                i+=1
                continue

            if s[i] not in st:
                if st[-1]< s[i]:
                    st.append(s[i])
                    i+=1

                else:
                    if st[-1] in s[i:]:
                        st.pop()
                    else:
                        st.append(s[i])
                        i+=1
            else:
                i+=1

        return "".join(st)

        