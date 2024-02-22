class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range (len(nums1)):
            n=nums2.index (nums1[i])
            if n==len(nums2)-1:
                ans.append (-1)


            for j in range (n+1,len(nums2),1):
                if nums1[i]<nums2[j]:
                    ans.append (nums2[j])
                    break
                elif j==len(nums2)-1:
                    ans.append (-1)
        return ans
                
        