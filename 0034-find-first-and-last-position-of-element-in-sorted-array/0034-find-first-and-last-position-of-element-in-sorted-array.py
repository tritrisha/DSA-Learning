class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=0
        y=len(nums)-1
        res=[-1,-1]
        n=0
        if x==y and target==nums[x]:
            return [0,0]
        while x<y+1:
            if nums[x]<target:
                x+=1
                print(x)
            elif nums[x]==target:
                res[0]=x
            
            
            if nums[y]>target:
                y-=1
            elif nums[y]==target:
                res[1]=y
                
                    
            if res[0]==x and res[1]==y:
                break
                    
        
        return res

            


            
                    





            


        
       

            


            






            
        
        