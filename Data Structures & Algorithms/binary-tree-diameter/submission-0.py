# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def dfs(node):

            nonlocal diameter

            if node is None:
                return 0
            
            path_left = dfs(node.left) 
            path_right = dfs(node.right)

            possible_diameter = path_left + path_right 

            if possible_diameter > diameter:
                diameter = possible_diameter

            return max(path_left + 1, path_right + 1)

        dfs(root)

        return diameter
