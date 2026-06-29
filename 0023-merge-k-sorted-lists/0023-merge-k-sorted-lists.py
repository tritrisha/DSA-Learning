# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r=[]
        for i in lists:
            c=i
            while c:
                r.append(c.val)
                c=c.next

        r.sort()
        
        if r:
            x=ListNode(r[0])
            print(x)
            c=x
            for i in r[1:]:
                c.next=ListNode(i)
                c=c.next

            return x

        else:
            return


        