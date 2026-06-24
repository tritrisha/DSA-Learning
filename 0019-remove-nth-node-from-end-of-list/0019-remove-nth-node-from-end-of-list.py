# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=0
        c=head
            
        while c:
            p+=1
            c=c.next
        c=head
        if p!=n:
            p=p-n
            print(p)
            while p:
                p-=1
                if p==0:
                    c.next=c.next.next
                c=c.next
            return head

        else:
            return head.next




        