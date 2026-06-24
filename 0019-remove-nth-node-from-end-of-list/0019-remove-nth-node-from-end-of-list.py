# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=head
        temp=head
        for _ in range(n):
            c=c.next
            
        if not c:
            return temp.next

        while c.next:
            c=c.next
            temp=temp.next

        temp.next=temp.next.next

        return head
        
        




        