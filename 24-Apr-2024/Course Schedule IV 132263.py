# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans =[set() for i in range(numCourses)]
        dect =defaultdict(list)
        outgo = defaultdict(int)

        for item ,to in prerequisites:
            dect[item].append(to)
            outgo [to] +=1
        que = deque()
        for i in range(numCourses):
            if outgo[i] ==0:
                que.append(i)
        
        while que:
            temp =que.popleft()
            for nigh in dect[temp]:
                outgo[nigh] -= 1
                ans[nigh].add(temp)
                ans[nigh].update(ans[temp])
                if outgo[nigh] == 0:
                    que.append(nigh)
        ans2=[]
        for pr,q in queries:
            if pr in ans[q]:
                ans2.append(True)
            else:
                ans2.append(False)

        return ans2






