class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        l=len(shifts)
        pre=[0]*(l+1)
        p=''
        for i in range(l-1, -1, -1):
            pre[i]=(pre[i+1]+shifts[i])
        for j in range(l):
            n=(ord(s[j])-ord('a')+pre[j])%26
            p+=chr(n+97)

        return p

        