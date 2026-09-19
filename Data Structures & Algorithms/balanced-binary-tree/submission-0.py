# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Idea is I use this variable to track whether the heigh in the right idfferes with more than 1
        max_diff = 0

        def diff_tree(node):
            nonlocal max_diff
            
            if not node:
                return 0
            
            left = diff_tree(node.left)
            right = diff_tree(node.right)

            diff = abs(right - left)
            max_diff = max(diff, max_diff)

            return 1 + max(left, right)

        
        diff_tree(root)
        return (max_diff <= 1)