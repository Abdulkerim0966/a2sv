# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used =[]
        use =0
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                heappush(used,-(heights[i]-heights[i-1]))
                use += (heights[i]-heights[i-1])
                
                if use > bricks:
                    if ladders == 0:
                        return i-1
                    else:
                        ladders -=1
                        temp=heappop(used)
                        use +=temp
        return (len(heights)-1)


        