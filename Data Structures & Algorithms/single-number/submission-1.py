class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR operation
        res = 0

        for n in nums:
            res ^= n
        
        return res
        