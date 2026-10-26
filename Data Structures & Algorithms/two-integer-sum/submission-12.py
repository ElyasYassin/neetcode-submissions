class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}

        for x in range(len(nums)):
            curr_remain = target - nums[x] 
            if curr_remain in remaining:
                return [remaining[target - nums[x]], x]
            
            else:
                remaining[nums[x]] = x

        return []