class Node:
    def __init__(self,value=0):
        self.val=value
        self.next=None
class MyLinkedList:


    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        ind=0
        currhead=self.head
        if self.head:
            while currhead.next and ind <index:
                currhead=currhead.next
                ind+=1
            if ind!=index:
                return -1
            return currhead.val
        return -1
    def addAtHead(self, val: int) -> None:
        if self.head:
            temp=Node(val)
            temp.next=self.head
            self.head=temp
        else:
            temp=Node(val)
            self.head=temp
        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        if self.head:
            while curr.next:
                curr=curr.next
            temp=Node(val)
            curr.next=temp
        else:
            self.addAtHead(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        ind=0
        curr=self.head
        if index==0:
            if self.head:
                temp=Node(val)
                temp.next=self.head
                self.head=temp
            else:
                temp=Node(val)
                self.head=temp
        else:
            if self.head:
                while curr.next and ind<index-1:
                    curr=curr.next
                    ind+=1
                
                if ind==index-1 and curr.next==None:
                    temp=Node(val)
                    curr.next=temp
                elif ind<index-1:
                    pass
                else:
                    temp=Node(val)
                    temp.next = curr.next
                    curr.next = temp
                curr=self.head

            while curr:

                print(curr.val)
                curr=curr.next
    def deleteAtIndex(self, index: int) -> None:
        ind=0
        if index==0:
            if self.head:
                self.head=self.head.next
        else:
            curr = self.head
            while curr.next and ind<index-1:
                curr=curr.next
                ind+=1
            if curr.next:
                curr.next=curr.next.next
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)