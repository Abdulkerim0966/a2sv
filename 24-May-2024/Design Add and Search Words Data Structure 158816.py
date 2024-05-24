# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

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


    def search(self,curr, word: str) -> bool:
   
        
        for idx,ch in enumerate (word):
            if ch != '.':
                if ch not in curr:
                    return False
            else:
                ans = False
                for key in curr :
                    if key != '#':
                        # print(key,curr[key])
                        ans |= self.search(curr[key],word[idx+1:])
                return  ans
            curr = curr[ch]
        return curr['#']

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

        

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(self.trie.root,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)