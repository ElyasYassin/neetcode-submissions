class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        
        l, r = 0, 0

        res = 0

        while r < len(s):
            chars[ord(s[r]) - ord("A")] += 1
        
            while ((r - l + 1) - max(chars)) > k:
                chars[ord(s[l]) - ord("A")] -= 1
                l += 1
                
        
            res = max(res, (r - l + 1))
            r += 1
        
        
        return res
        
         