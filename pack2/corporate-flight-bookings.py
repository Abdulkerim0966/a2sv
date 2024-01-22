class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flait=[0]*(n+1)
        for i in range(len(bookings)):
            flait[bookings[i][0]-1]+=bookings[i][2]
            flait[bookings[i][1]]-=bookings[i][2]
        for i in range(1,n+1):
            flait[i]+=flait[i-1]
        flait.pop(n)
        return flait



        