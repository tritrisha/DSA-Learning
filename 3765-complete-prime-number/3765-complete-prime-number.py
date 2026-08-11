class Solution:
    def completePrime(self, num: int) -> bool:
        def isitprime(n):
            if n<=1:
                return False
            for i in range(2, int(n**0.5)+1):
                if n%i==0:
                    return False

            return True


        x=num
        if isitprime(x):
            while x:
                if isitprime(x):
                    x//=10
                else:
                    return False

            x=str(num)
            while x:
                if isitprime(int(x)):
                    x=x[1:]

                else:
                    return False

            return True

        return False

            



        

        



        

        