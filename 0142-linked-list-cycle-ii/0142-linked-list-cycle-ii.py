# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        r=head
        if head==None or head.next==None:
            return 

        while r:
            t=t.next
            r=r.next.next
            if t==r:
                break

            elif r==None or r.next==None:
                return 
            

        while head!=t:
            t=t.next
            head=head.next

        return head

        

        
        
        

        




        