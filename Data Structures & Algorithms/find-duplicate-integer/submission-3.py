class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}

        for x in nums:
            if x in hashmap:
                return x
            
            else:
                hashmap[x] = 1