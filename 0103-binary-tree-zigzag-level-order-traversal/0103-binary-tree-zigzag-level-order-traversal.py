# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res=[]
        q=deque()
        q.append(root)
        c=0
        while q:
            r=[]
            for _ in range(len(q)):
                s=q.popleft()
                r.append(s.val)
                if s.right:
                    q.append(s.right)

                if s.left:
                    q.append(s.left)

            if c%2==0:
                r=r[::-1]

            res.append(r)
            c+=1

        return res

            
        