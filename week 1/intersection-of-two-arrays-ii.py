class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dect=defaultdict(int)
        
        ans=[]
        
        for i in range(len(nums1)):
            dect[nums1[i]]+=1
        for i in range(len(nums2)):
            if nums2[i] in dect and dect[nums2[i]]>0:
                dect[nums2[i]]-=1
                ans.append(nums2[i])
        return ans

                
