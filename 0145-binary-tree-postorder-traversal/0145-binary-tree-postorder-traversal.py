# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def poso(root):
            if not root:
                return 

            poso(root.left)
            poso(root.right)
            x.append(root.val)

            return

        x=[]
        poso(root)

        return x

        