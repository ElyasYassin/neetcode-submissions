class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # INPUT: nums: list of unique integers - ascending order
        #        target: int
        # FUNCTION: searches for target within nums
        # RETURN: index if exists, otherwise -1
        # CONSTRAINT: O(logn) time = binary search

        # Questions:
        # - list be one number?

        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        
        # setting left and right pointers
        l, r = 0, len(nums)
        
        while l < r:
            # setting midpoint
            m = (l + r) // 2

            if nums[m] < target:
                l += 1

            elif nums[m] > target:
                r -= 1

            else:
                return m

        return -1 

            

