class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod= 10**9 + 7
        poww=[1]*100001
        for i in range(1, 100001):
            poww[i]=(poww[i-1]*10) % mod
        sys.set_int_max_str_digits(50000)
        n=len(s)
        ps=[0]*(n)
        sstr=[0]*(n)
        zeroc=[1]*(n)
        
        for i in range(1, n):
            if s[i]!='0':
                zeroc[i]=zeroc[i-1]+1
            else:
                zeroc[i]=zeroc[i-1]        

        for i in range(n):
            ps[i]= ps[i-1]+ int(s[i])
            if s[i]!='0':
                sstr[i]=(sstr[i-1]*10 + int(s[i])) % mod
            else:
                sstr[i]=sstr[i-1]
        print(sstr)
        res=[0]*(len(queries))

        for i in range(len(queries)):
            r=queries[i][0]
            l=queries[i][1]
            if r!=0:
                lenofp=zeroc[l]-zeroc[r-1]
                summing=ps[l]-ps[r-1]
                res[i] = (sstr[l] - sstr[r-1] * poww[lenofp]) * (summing) %mod
            else:
                summing=ps[l]
                res[i] = (sstr[l]) * (summing) %mod

        return res

            

        

    



            


            
        


        