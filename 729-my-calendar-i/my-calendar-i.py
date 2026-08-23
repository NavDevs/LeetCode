class MyCalendar(object):

    def __init__(self):
        self.events = []
        

    def book(self, startTime, endTime):
        for s,e in self.events:
            if not(e <= startTime or  endTime <=s):
                return False
        self.events.append((startTime,endTime))
        return  True 
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)