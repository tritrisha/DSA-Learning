# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def ino(root):
            if not root:
                return 

            ino(root.left)
            x.append(root.val)
            ino(root.right)


            return 

        x=[]
        ino(root)
        return x
        