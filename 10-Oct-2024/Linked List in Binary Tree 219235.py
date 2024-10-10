# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution:
    def isSubPath(self, h: Optional[ListNode], r: Optional[TreeNode]) -> bool:
        f = lambda l,t:t and (g(l,t) or f(l,t.left) or f(l,t.right))
        g = lambda l,t:not l or (t and t.val==l.val and (g(l.next,t.left) or g(l.next,t.right)))

        return f(h, r)