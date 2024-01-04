class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n=len(nums)
        for i in range(n):
            if nums[i]%n ==0:
                continue
            right=i

            for j in range(n):
                print(i,right)
                

                right=(right+nums[right]) % n
                if nums[i]/nums[right] < 0:
                    break
                if i==right%n:
                    return True
        return False

        