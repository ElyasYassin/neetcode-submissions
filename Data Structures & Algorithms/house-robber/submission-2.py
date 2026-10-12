class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        self.profit = 0

        def dfs(i):
            if i > len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]
                     
            # skip
            skip = dfs(i + 1)

            # rob
            rob = nums[i] + dfs(i + 2)

            memo[i] = max(rob, skip)
            return memo[i]
    
        return dfs(0)
