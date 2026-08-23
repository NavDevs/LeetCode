class MyCalendarTwo(object):

    def __init__(self):
        self.events =[]
        self.double = []
        

    def book(self, startTime, endTime):

        for s , e in self.double:
            overlap_start =  max(startTime,s)
            overlap_end = min(endTime,e)

            if overlap_start < overlap_end:
                return False
        
        for s ,e in self.events:
            overlap_start =  max(startTime,s)
            overlap_end = min(endTime,e)

            if overlap_start < overlap_end:
                self.double.append((overlap_start, overlap_end))

        self.events.append((startTime,endTime))
        return True


        
