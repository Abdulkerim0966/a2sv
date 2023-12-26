class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        sets= set()
        for no in arr2:
            sets.add(no)
            for i in range(len(arr1)):
                if no==arr1[i]:
                    ans.append(arr1[i])
        arr = []
        for i in range (len(arr1)):
            if arr1[i] not in sets:
                arr.append(arr1[i])
        
        return ans + sorted(arr)
        