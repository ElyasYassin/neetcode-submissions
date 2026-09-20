class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # input: 2D characters board [[]]
        # output: True if word exists, else false
        # process: form the word with a path in the board using horizontal or vertical neighbors.

        # when we find the first letter that exists in the word, we look at the vneighbors and see if any align then 
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            # Every character in the word has been matched
            if i == len(word):
                return True

            # Invalid position or incorrect character
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != word[i]
            ):
                return False

            # Temporarily mark this cell as visited
            character = board[r][c]
            board[r][c] = "#"

            # Search all four neighboring cells
            found = (
                dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )

            # Restore the cell for other possible paths
            board[r][c] = character

            return found

        # Try starting from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
                    
    
