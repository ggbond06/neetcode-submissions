# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, greatest_value_seen_on_path):

            if node == None:
                return 0

            count = 0

            if node.val >= greatest_value_seen_on_path:
                greatest_value_seen_on_path = node.val
                count += 1

            count_left = helper(node.left, greatest_value_seen_on_path)
            count_right = helper(node.right, greatest_value_seen_on_path)

            return count_left + count_right + count
        
        return helper(root, root.val)