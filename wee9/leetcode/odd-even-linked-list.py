# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        curr=head
        curr2=head.next
        temp2=head.next
        temp=head
        
        while curr.next:
            if curr.next and curr.next.next:

                temp=curr.next
                curr.next=curr.next.next
                curr=curr.next
            
                if temp.next:
                    temp=temp. next
            else:
                curr=curr.next
            if curr2 and curr2.next and curr2.next.next:
                curr2.next=curr2.next.next
                curr2=curr2.next
              
            else:
                curr2.next=None
          
        temp.next=temp2
        return head