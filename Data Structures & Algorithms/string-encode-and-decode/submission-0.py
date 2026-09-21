class Solution:

    def encode(self, strs: List[str]) -> str:
        # idea: encode into integer+delimiter
        res = ""
        for x in strs:
            res += (f"{len(x)}#" + x)

        return res
    
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_word = int(s[i:j])
            print(length_word)
            res.append(s[j + 1:j + 1 + length_word])
            i = j + 1 + length_word 

        return res

        
                

