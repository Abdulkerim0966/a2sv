# Problem: Merge K Sorted List - https://leetcode.com/problems/merge-k-sorted-lists/

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
            temp= heappop(ans)
            curr.next = lists[temp[1]]
            curr = curr.next
            if lists[temp[1]].next :
                lists[temp[1]] = lists[temp[1]].next
                heappush(ans ,(lists[temp[1]].val ,temp[1]))

        return dummynode.next





        