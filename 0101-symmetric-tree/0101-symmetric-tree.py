# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftsub=[]
        rightsub=[]
        def dfs(node, sub):
            if not node:
                sub.append(-101)
                return 
            sub.append(node.val)
            dfs(node.left, sub)
            dfs(node.right, sub)

            return

        def rdfs(node, sub):
            if not node:
                sub.append(-101)
                return 
            sub.append(node.val)
            rdfs(node.right, sub)
            rdfs(node.left, sub)

            return
        
        dfs(root.left, leftsub)
        rdfs(root.right, rightsub)
        

        return leftsub==rightsub

        