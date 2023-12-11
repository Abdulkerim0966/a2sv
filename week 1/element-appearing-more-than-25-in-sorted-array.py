class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        no_exist=Counter(arr)
        return max(no_exist, key=no_exist.get)