# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for  i in range(len(lists)):
            if lists[i]:
                ans.append((lists[i].val,i))

        dummynode = ListNode()
        
        heapify(ans)
        curr =dummynode

        while ans:
            temp= heappop(ans)[1]
            curr.next = lists[temp]
            curr = curr.next
            if lists[temp].next :
                lists[temp] = lists[temp].next
                heappush(ans ,(lists[temp].val ,temp))

        return dummynode.next
