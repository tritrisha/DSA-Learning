# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vala=[]
        while head:
            vala.append(head.val)
            head=head.next

        ret=[0]*len(vala)
        stac=[]
        i=0
        while i<len(vala):
            if not stac:
                stac.append(i)
                i+=1
                continue

            if vala[stac[-1]]<vala[i]:
                x=stac.pop()
                ret[x]=vala[i]
            else:
                stac.append(i)
                i+=1

        return ret

            

            
                
            
            
            



            




            


        