class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        l=len(flowerbed)
        for i in range(l):
            if flowerbed[i]==0:
                if i==l-1:
                    if flowerbed[i-1]==0:
                        n-=1
                elif i==0:
                    if flowerbed[i+1]==0:
                        n-=1
                        flowerbed[i]=1

                elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    n-=1
                    flowerbed[i]=1

        return n<=0

        