# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = []
        curr = head
        su =0
        while curr:
            if zero:
                if curr.val == 0:
                    temp = zero.pop()
                    temp.next.val = su
                    temp.next.next = curr.next
                    su =0
                    zero.append(temp.next)
                else:
                    su += curr.val
            else:
                if curr.val ==0:
                    zero.append(curr)
            curr=curr.next
        if head.val == 0:
            return head.next

        else:
            return head





        