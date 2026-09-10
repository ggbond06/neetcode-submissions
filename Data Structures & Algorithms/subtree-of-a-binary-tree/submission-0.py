# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(node, subRoot):
            
            if node is None and subRoot is None:
                return True

            if node is None or subRoot is None:
                return False

            if node.val != subRoot.val:
                return False

            left = helper(node.left, subRoot.left)
            right = helper(node.right, subRoot.right)

            return left and right

        if root is None:
            return False
        
        if helper(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

         


            


            