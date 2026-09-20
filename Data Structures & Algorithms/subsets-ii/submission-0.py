class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = set()
        subset = []

        def dfs(i):
            if i >= len(nums):
                subsets.add(tuple(subset))
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return [list(s) for s in subsets]