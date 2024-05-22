# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms=[[0,i,0] for i in range(n)]
        heapify(rooms)
        meetings.sort()
        # print(meetings)
        for meet in meetings:
            
            temp1=[]
            while rooms and rooms[0][0] <=meet[0]:
                t =heappop(rooms)
                t[0] =0
                temp1.append(t)
            for iten in temp1:
                heappush(rooms,iten)

            temp=heappop(rooms)
            temp[0]+=((meet[1]-meet[0]) if temp[0]>meet[0]else meet[1])
            temp[2]+=1
            heappush(rooms,temp)

        rooms.sort(key=lambda x:(x[2],x[1]))
        # print(rooms)
        ans = rooms[-1][1]
        temp =-2
        while ans>0 and rooms[-1][2]==rooms[temp][2]:
            ans =rooms[temp][1]
            temp-=1
 
        return ans


        