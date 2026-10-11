class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26

        for x in s1:
            freq_s1[ord(x) - ord('a')] += 1

        print(freq_s1)

        i = 0
        while i + len(s1) <= (len(s2)):
            freq_s2 = [0] * 26

            for y in range(i, i+len(s1)):
                freq_s2[ord(s2[y]) - ord('a')] += 1
            
            print(freq_s2)
            
            if freq_s2 == freq_s1:
                return True

            i += 1
        
        return False
        
