class MinStack(object):

    def __init__(self):
        self.st  =[]
        self.minst =[]
        

    def push(self, value):
        self.st.append(value)
        if  not  self.minst or value<= self.minst[-1]:
            self.minst.append(value)
        else:
            self.minst.append(self.minst[-1])


        
        """
        :type value: int
        :rtype: None
        """
        

    def pop(self):
        self.st.pop()
        self.minst.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.st[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        
        return self.minst[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()