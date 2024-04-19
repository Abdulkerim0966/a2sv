# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend =set(deadends)
        dect = {'0':['1','9'] , '1':['0','2'] , '2':['1','3'] ,'3':['2','4'], '4':['3','5'] , '5':['4','6'], '6':['5','7'], '7':['6','8'], '8':['7','9'], '9':['8','0']}
        que =deque(['0000'])
        visited = {'0000'}
        if '0000' in deadend:
            return -1
        count =0
        while que:
            
            for i in range(len(que)):
                temp =que.popleft()
            
                if temp ==target:
                    return count
                
                for i  in range(4):
                    for nigh in dect[temp[i]]:
                        temp2 = temp[:i] + nigh + temp[i+1:]
                        if temp2 not in visited and temp2 not in deadend:
                            que.append(temp2)
                            visited.add(temp2)
            count +=1
        return -1

                    
        