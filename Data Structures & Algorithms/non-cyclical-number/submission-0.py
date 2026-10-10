class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            summ = 0
            for x in str(n):
                summ += int(x) ** 2

            seen.add(n)

            n = summ

        return True