# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.root = {}
        self.ans =[]
        self.set=set()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        self.set.add(word)
        


    def search(self,curr,temp) -> bool:
        
        if not curr:
            self.ans.append(''.join(temp))

        
        for ch in curr:
            temp.append (ch)
            if ''.join(temp) not in self.set:
                temp.pop()
                
                self.ans.append(''.join(temp))
                continue
            self.search(curr[ch],temp)
            temp.pop()
       
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie =Trie()
        for word in words:
            trie.insert(word)
        
        trie.search(trie.root,[])
        ans =trie.ans
        ans.sort(key=lambda x:len(x),reverse =True)
        temp =[]
        temp.append(ans[0])
        for i in range(1,len(ans)):
            if len(ans[i]) == len(ans[i-1]):
                temp.append(ans[i])
            else:
                break
     
        temp.sort()
        return temp[0]
        

        
        