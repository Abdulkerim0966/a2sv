# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dect =defaultdict(list)
        incom =defaultdict(int)
        for c in prerequisites:
            dect[c[1]].append(c[0])
            incom[c[0]] +=1


        que =deque()
        for i in range(numCourses):
            if i not in incom:
                que.append(i)

        ans =[]
        print(que)
        while que:
            temp =que.popleft()
            ans.append(temp)
            for nigh in dect[temp]:

                incom[nigh]-=1
                if incom[nigh] == 0:
                    que.append(nigh)
        print(ans)
        return ans if len(ans) == numCourses else []









        