class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        stack.append([nums[0],0])
        min_=[]
        min_.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]<min_[-1]:
                min_.append(nums[i])
            else:
                min_.append(min_[-1])
            while stack and stack[-1][0]<=nums[i]:
                stack.pop()
            stack.append([nums[i],i])
            if len(stack)>=2:
                if stack[-1][0]>min_[stack[-2][1]] and stack[-1][0]!=stack[-2][0]:
                    return True

        return False

        