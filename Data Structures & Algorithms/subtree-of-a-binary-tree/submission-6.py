# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #subroot is empthy
        if not subRoot:
            return True

        #root is empthy
        if not root:
            return False
        #check if current node = subtree
        if self.sameTree(root,subRoot):
            return True

        #recursion

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        



    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        #recursive check left than right
        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        