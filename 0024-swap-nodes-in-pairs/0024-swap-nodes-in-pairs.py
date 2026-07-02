# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if head.next==None:
            return head
        dum=ListNode(0)
        prev=dum
        c=head
        
        
        while c and c.next:
            n=c.next
            print(n)
            s=n.next

            n.next=c
            c.next=s
            prev.next=n

            prev=c
            c=s


        return dum.next



            
            
        

        



        