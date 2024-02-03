# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        curr=head
        while head:
            curr=head
            head=head.next
            curr.next=temp
            temp=curr
            
        # print(head,curr)
        return curr
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head= self.reverseList(head)
        demmynode=ListNode(2,head)
        temp=demmynode
        p=0
        curr=demmynode
        while curr and  p<n:
            temp=curr
            p+=1
            curr=curr.next
        temp.next=curr.next
        return self.reverseList(demmynode.next)
