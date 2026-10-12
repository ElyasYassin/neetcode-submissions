# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Traverse the whole tree using BFS then get the kth element per level
        res = []
        
        nodes = deque()
        nodes.append(root)

        while nodes:
            qlen = len(nodes)

            for x in range(qlen):
                node = nodes.popleft()

                if node:
                    res.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
            
            
        res.sort()
        print(res)
        return res[k - 1]