class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[-1]*len(nums2)
        for i in range(len(nums2)):
            if len(stack)==0 or nums2[i]<stack[-1][0]:
                stack.append([nums2[i],i])
            else:
                while stack and nums2[i]>stack[-1][0]:
                    ans[stack[-1][1]]=(nums2[i])
                    stack.pop()
                stack.append([nums2[i],i])
        for i in range(len(nums1)):
            nums1[i]=ans[nums2.index(nums1[i])]
        return nums1
        