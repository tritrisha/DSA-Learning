# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preord(root):
            if not root:
                x.append("n")
                return

            x.append(root.val)
            preord(root.left)
            preord(root.right)
            return

        x=[]
        preord(p)
        s=x
        print(s)
        x=[]
        preord(q)
        print(x)
        if s!=x:
            return False
        return True



        