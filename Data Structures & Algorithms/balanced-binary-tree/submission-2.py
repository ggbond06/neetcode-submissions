# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.getHeight(root.left) + 1
        right_height = self.getHeight(root.right) + 1

        return max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        left_balance = self.isBalanced(root.left)
        right_balance = self.isBalanced(root.right)

        if abs(left_height - right_height) <= 1 and left_balance and right_balance:
            return True
        else:
            return False

    