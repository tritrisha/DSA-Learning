class Solution:
    def clearDigits(self, s: str) -> str:
        k=[]
        for i in s:
            if i.isalpha():
                k.append(i)

            else:
                k.pop()


        return "".join(k)


        