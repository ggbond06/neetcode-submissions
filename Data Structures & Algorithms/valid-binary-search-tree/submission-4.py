# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lower_bound, upper_bound):
            if node == None:
                return True

            if node.val <= lower_bound or node.val >= upper_bound:
                return False

            if node.left != None:
                if node.left.val >= node.val:
                    return False

            if node.right != None:
                if node.right.val <= node.val:
                    return False

            left = helper(node.left, lower_bound, node.val)
            right = helper(node.right, node.val, upper_bound)

            return left == True and right == True

        return helper(root, float("-inf"), float("inf"))
