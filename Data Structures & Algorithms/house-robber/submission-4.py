class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            # rob
            rob = nums[i] + dfs(i + 2)

            # skip
            skip = dfs(i + 1)

            memo[i] = max(rob, skip)

            return memo[i]

        return dfs(0)