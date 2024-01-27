# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        demmynode=ListNode(-200,head)
        curr=demmynode
        print(head)
        temp=curr
        while curr and curr.val<x:
            temp=curr
            curr=curr.next
        temp2=curr
        if curr:
            curr=curr.next
        while curr:
            if curr.val<x:
                if temp==demmynode:
                    head =curr

                temp2.next=curr.next
                curr.next=temp.next
                temp.next=curr
                temp=curr
                curr=temp2.next
            else:
                temp2=curr
                curr=curr.next
        return head
        
            


        
   

        