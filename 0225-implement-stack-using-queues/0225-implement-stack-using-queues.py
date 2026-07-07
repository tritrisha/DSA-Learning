class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1)!=1:
            self.q2.append(self.q1.pop(0))
        r=self.q1.pop(0)
        while self.q2:
            self.q1.append(self.q2.pop(0))
        return r

    def top(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()