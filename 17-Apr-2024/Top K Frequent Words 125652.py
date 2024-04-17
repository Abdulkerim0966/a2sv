# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dect = defaultdict(int)
        for i in range(len(words)):
            dect[words[i]]+=1
        words.sort()
        words.sort(key=lambda x:dect[x],reverse=True)
        ans =[]
        se =set()
        count =0
        i =0
        while count <k :

            if words[i] not in se:
                ans.append(words[i])
                se.add(words[i])
                count +=1
            i+=1
            
        
        return ans
        