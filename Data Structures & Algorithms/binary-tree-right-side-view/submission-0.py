# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def helper_append_right(node, depth):

            if node is None:
                return 

            if depth == len(output):
                output.append(node.val)

            helper_append_right(node.right, depth+1)
            helper_append_right(node.left, depth+1)

        helper_append_right(root, 0)

        return output



        