# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.curr_lowest = root

        def dfs(node):
            if not node:
                return

            # if both values are smaller than root, we change lowest to left then move to left child
            if p.val < node.val and q.val < node.val:
                dfs(node.left)

            # if both values are bigger than root, we change lowest to right then move to right child
            elif p.val > node.val and q.val > node.val:
                dfs(node.right)

            # if it's equal to one of them then we set that as a root then return
            elif node.val == p.val or node.val == q.val:
                self.curr_lowest = node
                return 

            # If left is smaller and right is bigger
            else:
                self.curr_lowest = node
                return


        dfs(root)
        return self.curr_lowest
            
