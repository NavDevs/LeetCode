class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]
        
        

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        
        

    def pop(self):
        if not self.s1:
            return -1
        return self.s1.pop()

    def peek(self):
        if not self.s1:
            return -1
        return self.s1[-1]


        

    def empty(self):
        return not self.s1 
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()