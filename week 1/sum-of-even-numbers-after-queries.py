class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]  
        count=0     
        for j in range(len(nums)):
                if nums[j]%2==0:
                    count+=nums[j]
            
        for i in range(len(queries)):
            if nums[queries[i][1]]%2==1:
                if (nums[queries[i][1]]+queries[i][0])%2==0:
                    count+=nums[queries[i][1]]+queries[i][0]
                    ans.append(count)
                else:
                    ans.append(count)

            elif nums[queries[i][1]]%2==0:
                if (nums[queries[i][1]]+queries[i][0])%2==0:
                    count+=queries[i][0]
                    ans.append(count)
                else:
                    count-=nums[queries[i][1]]
                    ans.append(count)
            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]
             
            
            
        return ans