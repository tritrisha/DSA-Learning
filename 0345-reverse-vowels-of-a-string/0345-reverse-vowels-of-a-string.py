class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                vowel.append(i)

            if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                vowel.append(i)


        vowel=vowel[::-1]
        p=0
        k=''
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                k+=vowel[p]
                p+=1

            else:
                k+=i


        return k



        