# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode=ListNode(2,head)
        curr=dummynode
        p=0
        while curr and p<left-1:
            curr=curr.next
            p+=1
        if curr.next==None or curr.next.next==None:
            return head
        else:
            temp=curr.next
            curr2=curr.next.next
            # temp2=curr2
            curr3=curr2
            temp3=temp
            while curr2 and p<right-1:
                curr3=curr2.next
                curr2.next=temp3
                temp3=curr2
                curr2=curr3
                p+=1
            curr.next=temp3
            temp.next=curr3

        return dummynode.next
        