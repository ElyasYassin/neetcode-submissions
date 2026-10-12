# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.bad_nodes = 0 
        self.nodes = 0

        def dfs(node, val):
            if not node:
                return
            
            self.nodes += 1

            if node.val < val:
                self.bad_nodes += 1

            val = max(node.val, val)

            dfs(node.left, val)
            dfs(node.right, val)

            return val
        
        dfs(root, root.val)

        return self.nodes - self.bad_nodes



        