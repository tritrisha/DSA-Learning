# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        c=head
        while c:
            c=c.next
            n+=1

        print(n)

        if n==1:
            return head
        
        if n%2!=0:
            t=head.next
            r=head.next.next
            while r.next!=None:
                t=t.next
                r=r.next.next


            return t

        head=head.next
        n=n-1
        if n==1:
            return head
        
        else:
            t=head.next
            r=head.next.next
            while r.next!=None:
                t=t.next
                r=r.next.next


            return t



        
        
        