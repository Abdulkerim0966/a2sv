class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num="".join(map(str,digits))
        nums=int(num)+1
        num=str(nums)
        ans=(int(x)  for x in num)

        return (ans)
        