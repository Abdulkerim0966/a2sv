class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def noOnes(number):
            bi=bin(number)
            return bi.count('1')
        arr.sort(key=lambda x:noOnes(x))
        return arr
    
            
        