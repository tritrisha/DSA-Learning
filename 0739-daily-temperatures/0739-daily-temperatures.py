class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        sta=[]
        for i in range(n):
            while sta and temperatures[sta[-1]]<temperatures[i]:
                j=sta.pop()
                ans[j]=i-j
            sta.append(i)


        return ans

                





        return ans

            



        