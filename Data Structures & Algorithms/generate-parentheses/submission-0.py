class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(curr, opened, closed):
            if len(curr) == n * 2:
                results.append(curr)
                return

            if opened < n:
                dfs(curr + "(", opened + 1, closed)
            
            if closed < opened:
                dfs(curr + ")", opened, closed + 1)

            return
        
        dfs("", 0, 0)
        return results

            
