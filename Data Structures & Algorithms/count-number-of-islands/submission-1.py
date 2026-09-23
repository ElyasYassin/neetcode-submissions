from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Assumptions: all edges are water - 
        # Algo: BFS 
        # If we find 1, then we perform BFS to see where we end up for each direction (we keep chasing ones). As we're doing this we want to make them as visited. Once we find the end, we increment the num_islands var by 1.
        
        rows, cols = len(grid), len(grid[0]) 
        visited = set()

        n_islands = 0

        directions = [
            (1, 0),   # Down
            (-1, 0),  # Up
            (0, 1),   # Right
            (0, -1)   # Left
        ]

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))

            while queue:
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    valid_neighbor = (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited
                    )

                    if valid_neighbor:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))



        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(x, y)
                    n_islands += 1
        
        return n_islands

        
