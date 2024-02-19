# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dect={}
        curr=headA
        
        while curr:
            dect[curr]=curr.val
            curr=curr.next
        curr=headB
        # print (dect)
        while curr:
            if curr in dect:
                return curr
            else:
                curr=curr.next

        