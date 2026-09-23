# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for this problem, we need to maintain levels as we just look at the rightmost element per level so BFS seems to be my go to solution
        q = deque()
        q.append(root)
        res = []

        while q:
            level = []
            len_q = len(q)
            
            for x in range(len_q):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
        
        results = []

        for x in res:
            results.append(x[-1])
        
        return results


