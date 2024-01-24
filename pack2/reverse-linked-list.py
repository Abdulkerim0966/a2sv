# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
            



        