class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        r=[]
        for i in s:
            if i=='(' and c>0:
                r.append(i)

            if i==')' and c>1:
                r.append(i)


            if i=='(':
                c+=1
            else:
                c-=1


        return ''.join(r)
            

                

            


        
            