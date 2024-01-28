# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        denmynode=ListNode(-6000,head)
        curr=denmynode
        temp=head.next
        while curr.next and curr.next.next:
            temp2=curr.next
            while temp:
                if temp.val<curr.next.val:
                    temp2.next=temp.next

                    # curr.next.next=temp.next
                    temp.next=curr.next
                    curr.next=temp
                    temp=temp2.next
                else:
                    temp2=temp
                    temp=temp.next

                # p=denmynode
                # print("head",p.next.val)
                # while p:
                #     print(p.val)
                #     p=p.next
                # print(curr.val,temp)
            curr=curr.next
            temp=curr.next.next
           
           
           
            
        return denmynode.next
        