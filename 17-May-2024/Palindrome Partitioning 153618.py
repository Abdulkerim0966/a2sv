# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def checker(s):
            left = 0
            right =len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right -=1
            return True
            
        ans =[] 
        bucket =[]      
        def back(st):
            if st ==len(s):
                ans.append(bucket.copy())
                return st

            for i in range(st+1,len(s)+1):
                # print('here',i,s[st:i])

                bucket.append(s[st:i])
                # print(bucket)
                back(i)
                bucket.pop()

        back(0)
        temp =[]
        for item in ans:
            for i in item:
                if not checker(i):
                    break
            else:
                temp.append(item)

        return temp










        