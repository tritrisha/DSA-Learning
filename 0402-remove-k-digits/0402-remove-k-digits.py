class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[num[0]]
        for i in range(1, len(num)):
            while s and s[-1]>num[i] and k:
                s.pop()
                k-=1

            s.append(num[i])

        while k:
            s.pop()
            k-=1

        if not s or len(s)==s.count('0'):
            return "0"

        return "".join(s).lstrip("0")


        