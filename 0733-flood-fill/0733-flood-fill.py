class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r, c= len(image), len(image[0])
        q=deque()
        q.append([sr, sc])
        direc=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        ori=image[sr][sc]
        if ori==color:
            return image
        image[sr][sc]=color
        while q:
            i, j=q.popleft()
            for x, y in direc:
                ni=i+x
                nj=j+y
                if ni<0 or nj<0 or ni>=r or nj>=c or image[ni][nj]!=ori:
                    continue
                
                image[ni][nj]=color
                q.append([ni, nj])

        return image

        

                

            

        