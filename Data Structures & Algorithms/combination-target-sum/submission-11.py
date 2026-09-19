class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        curr_sum = 0

        def dfs(i):
            nonlocal curr_sum
            nonlocal combinations
            nonlocal combination

            if i >= len(nums):
                return
            
            if sum(combination) == target:
                combinations.append(combination.copy())
                return
            
            if sum(combination)> target:
                return

            # go to next number
            combination.append(nums[i])
            added = nums[i]
            curr_sum += added
            dfs(i)

            # Stay in current number
            value = combination.pop()
            curr_sum -= value
            dfs(i + 1)

        dfs(0)
        return combinations