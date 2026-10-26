class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two strings: s and t
        first_word_anagram = [0] * 26
        second_word_anagram = [0] * 26

        for x in s:
            first_word_anagram[ord(x) - ord('a')] += 1
        for y in t:
            second_word_anagram[ord(y) - ord('a')] += 1
        
        return first_word_anagram == second_word_anagram