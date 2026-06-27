class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x=[]
        p=-1
        for i in range(len(operations)):
            if operations[i]=='C':
                x.pop() 
                p-=1 

            elif operations[i]=='D':
                x.append(2*int(x[p]))
                p+=1

            elif operations[i]=='+':
                if len(x)>1:
                    x.append(int(x[p])+int(x[p-1]))
                    p+=1

                else:
                    x.append(int(x[p]))
                    p+=1


            else:
                x.append(int(operations[i]))
                p+=1

        return sum(x)

