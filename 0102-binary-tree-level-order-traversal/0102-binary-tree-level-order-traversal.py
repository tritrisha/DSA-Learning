# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r=[]
        if not root:
            return r

        q=deque()
        q.append(root)
        while q:
            level=[]
            for _ in range(len(q)):
                e=q.popleft()
                level.append(e.val)
                
                if e.left:
                    q.append(e.left)

                if e.right:
                    q.append(e.right)

            r.append(level)

        return r



        




        
        


        