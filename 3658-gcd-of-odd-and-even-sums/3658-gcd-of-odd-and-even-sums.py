class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=n*n
        sumEven=n*n+n
        def gcd(sumEven, sumOdd):
            if sumEven==sumOdd:
                return sumEven
            if sumOdd==0:
                return sumEven
            if sumEven==0:
                return sumOdd
            if sumOdd<sumEven:
                return gcd(sumEven-sumOdd , sumOdd)
            return gcd(sumEven, sumOdd-sumEven)

        
        return gcd(sumEven, sumOdd)
        
        

        
        

        