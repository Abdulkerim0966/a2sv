# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[None]*k
        curr=head
        no=0
        while curr!=None:
            curr=curr.next
            no+=1
        print(no)
        extra=no%k
        curr=head
        ma=no//k
        i=0
        while curr!=None:
            temp=0
            if extra>0:
                ans[i]=curr
                temp2=curr
                while temp<=ma:
                    temp2=curr
                    curr=curr.next
                    temp+=1
                temp2.next=None
                extra-=1
            else:
                ans[i]=curr
                temp2=curr
                while temp<ma:
                    temp2=curr
                    curr=curr.next
                    temp+=1
                temp2.next=None
            i+=1

        return ans
        
        