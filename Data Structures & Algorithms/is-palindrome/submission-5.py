class Solution:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        # process the word first: lower case everything and remove non alphanumeric characters
        s = s.lower()
        processed_s = ""
        
        for char in s:
            if char.isalnum():
                processed_s += char
        
        # validate if palindrome
        p1, p2 = 0, len(processed_s) - 1

        while p1 <= p2:
            if processed_s[p1] != processed_s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True