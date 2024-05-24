# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Trie:
    def __init__(self):
        self.root = {'#':0}
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {'#':0}
            curr = curr[ch]
        curr['#'] = 1


    def search(self, word: str) -> bool:
 

        curr = self.root
        for idx, ch in enumerate (word):
          
            if ch not in curr:
             
                return len(word)
            elif curr[ch]['#']:
                
                return idx+1
            curr = curr[ch]
        return len(word)

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
        



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie =Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        ans = sentence.split()
        for i in range(len(ans)):
            idx =trie.search(ans[i])
         
            ans[i] =ans[i][:idx]
        return ' '.join (ans)

        
        
        