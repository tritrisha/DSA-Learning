class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        one=len(arr1)
        two=len(arr2)
        ans=0
        for i in range(one):
            for j in range(two):
                if abs(arr1[i]-arr2[j])<=d:
                    ans+=1
                    break


        return one-ans


        
                    

        