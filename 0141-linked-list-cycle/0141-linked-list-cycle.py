# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t=head
        rab=head
        while rab:
            if rab.next==None or t.next==None:
                    return False            
            
            t=t.next
            rab=rab.next.next

            if t==rab:
                return True

        

            
                

            

            