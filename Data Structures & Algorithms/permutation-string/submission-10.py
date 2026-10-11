class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for x in s1:
            freq_s1[ord(x) - ord('a')] += 1

        for y in s2[:len(s1)]:
            freq_s2[ord(y) - ord('a')] += 1

        if freq_s1 == freq_s2:
            return True

        i = 1

        while i + len(s1) <= len(s2):
            freq_s2[ord(s2[i - 1]) - ord('a')] -= 1
            freq_s2[ord(s2[i + len(s1) - 1]) - ord('a')] += 1

            if freq_s1 == freq_s2:
                return True

            i += 1
        
        return False

