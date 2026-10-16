class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(start, end, nums=nums):
            memo = {}

            nums = nums[start:end]

            def dfs(i):
                if i in memo:
                    return memo[i]

                if i >= len(nums):
                    return 0

                rob = nums[i] + dfs(i + 2) 
                skip = dfs(i + 1)

                memo[i] = max(rob, skip)
                return memo[i]
            
            return dfs(0)


        return max(helper(0, len(nums) - 1), helper(1,len(nums)))