class Solution:
    def fib(self, n: int) -> int:
        arr=[-1]*(n+1)
        arr[0]=0
        if n>0:
            arr[1]=1
        def fab(n):
            if n==1 or n==0:
                return arr[n]
            print(n)
            if arr[n]==-1:
                arr[n]=fab(n-1)+fab(n-2)
        
            return arr[n]

        return fab(n)
    



    
        