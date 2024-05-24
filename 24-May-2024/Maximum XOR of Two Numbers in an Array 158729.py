# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

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
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return curr['#']

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie =Trie()
        temp = '0000000000000000000000000000000'
        for num in nums:
            bi =str(bin(num)[2:])
            n =len(bi)
            trie.insert(temp[:31-n]+bi)
        
        ma =0
        for num in nums:
            bi =str(bin(num)[2:])
            n =len(bi)
            bi = temp[:31-n]+bi
        
            ans = []
            curr = trie.root
          
            for i in bi:
                if i == '1' and '0' in curr:
                    ans.append('1')
                    curr = curr['0']
                elif  i== '0' and '1' in curr:
                    ans.append('1')
                    curr =curr['1']
                else:
                    if  '0' in curr:
                        curr =curr['0']
                    elif '1' in curr:
                        curr = curr['1']
                    ans.append('0')
           
            ma = max(ma,int(''.join(ans),2))
        return ma

                    

                




        




            

     
        