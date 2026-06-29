class Solution:
    def longestValidParentheses(self, s: str) -> int:
        r=[-1]
        maxlen=0
        for i in range(len(s)):
            if s[i]=='(':
                r.append(i)


            else:
                r.pop()
                if not r:
                    r.append(i)
                else:
                    maxlen= max(maxlen, i-r[-1])


        return maxlen

        

        

        

        