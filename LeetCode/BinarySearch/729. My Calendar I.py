'''
https://leetcode.com/problems/my-calendar-i/description/
'''

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0
        right = len(self.bookings) - 1
        idx = len(self.bookings)

        while left <= right:
            mid = (left + right) // 2
            if self.bookings[mid][0] >= startTime:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if (idx > 0 and  self.bookings[idx-1][1] > startTime):
            return False
        if (idx < len(self.bookings) and self.bookings[idx][0] < endTime ):
            return False

        self.bookings.insert(idx,(startTime,endTime))
        return True
       

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
