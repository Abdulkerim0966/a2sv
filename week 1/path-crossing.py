class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dect=set()
        dect.add((0,0))
        x=0
        y=0
        for i in range(len(path)):
            if path[i]=='N':
                x+=1
                if (x,y) in dect:
                    return True
                dect.add((x,y))
            elif path[i]=='S':
                x-=1
                if (x,y) in dect:
                    return True
                dect.add((x,y))
            elif path[i]=='E':
                y+=1
                if (x,y) in dect:
                    return True
                dect.add((x,y))
            elif path[i]=='W':
                y-=1
                if (x,y) in dect:
                    return True
                dect.add((x,y))
            
        print(dect)        
            
        return False
           



        