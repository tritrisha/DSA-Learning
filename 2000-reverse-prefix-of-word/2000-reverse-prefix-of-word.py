class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=0
        for i in range(len(word)):
            if word[i]==ch:
                ind=i+1
                break

        x=word[:ind][::-1] + word[ind:]
        return x
        