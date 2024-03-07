class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxi=len(citations)-1
        mini=0
        n=len(citations)
        while mini<=maxi:
            mid=(maxi +mini)//2
            idx=bisect_left(citations,mid)
            if citations[mid]>=(n-mid):
                maxi=mid-1
            else:
                mini=mid+1
        return (n-mini)
    
        