class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = 0
        
        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]
            
            one_step = cost[i] + dfs(i + 1)
            two_steps = cost[i] + dfs(i + 2)

            memo[i] = min(one_step, two_steps)
        
            return memo[i]

        start_at_zero = dfs(0)
        start_at_one = dfs(1)

        return min(start_at_zero, start_at_one)