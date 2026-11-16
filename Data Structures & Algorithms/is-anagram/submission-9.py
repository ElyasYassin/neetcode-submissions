class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: s (str) and t (str)
        # could strings be empty?
        # are strings always the same length?
        # case sensitive?

        # idea: use hashmaps to store frequency for each (O(n)) then compare the hashmaps, if equal then True, else then False

        freq_s = {}
        freq_t = {}

        for char_s in s:
            if char_s in freq_s:
                freq_s[char_s] += 1
            
            else:
                freq_s[char_s] = 1
        
        for char_t in t:
            if char_t in freq_t:
                freq_t[char_t] += 1
            
            else:
                freq_t[char_t] = 1

        return freq_s == freq_t
