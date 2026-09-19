# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def subtreeHeight(root):
                nonlocal max_sum

                if not root:
                    return 0
                left = subtreeHeight(root.left)
                right = subtreeHeight(root.right)

                max_sum = max(max_sum, left + right)
                
                return 1 + max(left, right)
            
        subtreeHeight(root)
        return max_sum