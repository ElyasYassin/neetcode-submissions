from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Assumptions: all edges are water - 
        # Algo: BFS 
        # If we find 1, then we perform BFS to see where we end up for each direction (we keep chasing ones). As we're doing this we want to make them as visited. Once we find the end, we increment the num_islands var by 1.
        
        rows, cols = len(grid), len(grid[0]) 
        visited = set()

        n_islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                for x in range(len(q)):
                    # We want to all the neighbors to the queue
                    node = q.popleft()
                    
                    # bottom
                    if node[0] + 1 < rows and grid[node[0] + 1][node[1]] == "1" and (node[0] + 1, node[1]) not in visited:
                        q.append((node[0] + 1, node[1]))
                        visited.add((node[0] + 1, node[1]))
                    # right
                    if node[1] + 1 < cols and grid[node[0]][node[1] + 1] == "1" and (node[0], node[1] + 1) not in visited:
                        q.append((node[0], node[1] + 1)) 
                        visited.add((node[0], node[1] + 1)) 
                    # left
                    if node[1] - 1 >= 0 and grid[node[0]][node[1] - 1] == "1" and (node[0], node[1] - 1) not in visited:
                        q.append((node[0], node[1] - 1)) 
                        visited.add((node[0], node[1] - 1)) 
                    # top
                    if node[0] - 1 >= 0 and grid[node[0] - 1][node[1]] == "1" and (node[0] - 1, node[1]) not in visited:
                        q.append((node[0] - 1, node[1])) 
                        visited.add((node[0] - 1, node[1])) 



        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(x, y)
                    n_islands += 1
        
        return n_islands

        
