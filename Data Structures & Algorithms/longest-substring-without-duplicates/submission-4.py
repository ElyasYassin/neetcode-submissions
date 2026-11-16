class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: s (str)
        # Process: 
        # - finding length of all substrings without duplicate characters
        # - finding max length
        # return length of longest substring without duplicate characters


        # "zxyzxyz"
        #  ^^

        # "xxxx"
        #   ^^

        # constant that tracks max substring length
        # hashmap  

        charSet = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_length = max(max_length, r - l + 1)
        
        return max_length


        


