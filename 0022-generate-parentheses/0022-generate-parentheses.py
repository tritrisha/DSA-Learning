class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def para(o, c, r):
            if o==c==n:
                s.append(r)
                return 

            if o<n:
                para(o+1, c, r+'(')

            if c<o:    
                para(o, c+1, r+')')
                  
        s=[]
        para(0,0,'')
        return s
        


        

        