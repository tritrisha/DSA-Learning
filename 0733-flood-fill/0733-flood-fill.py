class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        p=image[sr][sc]
        def dfs(sr, sc):
            if image[sr][sc]==color:
                return 
            elif image[sr][sc]==p:
                image[sr][sc]=color
                if sr-1>=0:
                    dfs(sr-1, sc)

                if sr+1<len(image):
                    dfs(sr+1, sc) 
                    
                if sc+1<len(image[0]):
                    dfs(sr, sc+1)

                if sc-1>=0:
                    dfs(sr, sc-1)

        
        dfs(sr, sc)
        return image

        



            





        

        