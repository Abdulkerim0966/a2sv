# Definition for singly-linked list.
import copy
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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = copy.deepcopy(head)
        temp = self.reverseList(temp)
        while temp:
            if temp.val !=  head.val:
                return False
            temp=temp.next
            head=head.next
        return True
        
        
        