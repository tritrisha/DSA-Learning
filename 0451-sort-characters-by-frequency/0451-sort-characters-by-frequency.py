class Solution:
    def frequencySort(self, s: str) -> str:
        k={}
        for i in s:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        print(k)
        
        s=''
        for i in sorted(k, key=k.get, reverse=True):
            s+=i * k[i]

        return s
            

            