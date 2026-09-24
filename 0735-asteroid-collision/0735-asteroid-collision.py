class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        i=0
        l=len(asteroids)
        while i<l:
            if not stack:
                stack.append(asteroids[i])
                i+=1
                continue
            
            if asteroids[i]>0:
                stack.append(asteroids[i])
                i+=1
                    
            elif asteroids[i]<0:
                if stack[-1]<0:
                    stack.append(asteroids[i])
                    i+=1
                    continue
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()

                if stack and stack[-1]>0 and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                    i+=1

                elif stack and stack[-1]>0 and stack[-1]>abs(asteroids[i]):
                    i+=1

                

                

        return stack