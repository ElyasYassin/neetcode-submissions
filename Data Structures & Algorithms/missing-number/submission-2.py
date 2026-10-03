class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        
        nums.sort()
        for x in nums:
            if n != x:
                return n
            n += 1
        
        return n
        