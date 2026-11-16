class Solution:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        # process the word first: lower case everything and remove non alphanumeric characters
        s = s.lower()
        # validate if palindrome
        p1, p2 = 0, len(s) - 1

        while p1 <= p2:
            if not (s[p1].isalnum()):
                p1 += 1
                continue
            if not (s[p2].isalnum()):
                p2 -= 1
                continue

            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True