class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for x in strs:
            freq = [0] * 26
            for y in x:
                freq[ord(y) - ord('a')] += 1
            
            if tuple(freq) in hashmap:
                hashmap[tuple(freq)].append(x)
            
            else:
                hashmap[tuple(freq)] = [x]
            
        return list(hashmap.values())
            
    