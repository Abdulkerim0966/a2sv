class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dect={}
        for i in range(len(nums)):
            dect[nums[i]]=i
        for i in range(len(operations)):
            ind=dect[operations[i][0]]
            nums[dect[operations[i][0]]]=operations[i][1]

            dect[operations[i][1]]=ind
            del dect[operations[i][0]]
      
        return nums    
        