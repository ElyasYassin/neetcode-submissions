class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for x in range(len(nums)):
            if target - nums[x] in diff:
                return [diff[target - nums[x]], x]
            else:
                diff[nums[x]] = x 
        
        