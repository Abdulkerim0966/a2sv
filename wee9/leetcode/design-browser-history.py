class ListNode:
    def __init__(self, val=0, next=None,pre=None):
        self.val = val
        self.next = next
        self.pre=pre
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=ListNode(homepage)
        self.curr=self.head

    def visit(self, url: str) -> None:
        temp=ListNode(url,None,self.curr)
        self.curr.next=temp
        self.curr=temp
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr!=self.head:
                self.curr=self.curr.pre
            else:
                break
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr=self.curr.next
            else:
                break
        return self.curr.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)