class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for x in range(n + 1):
            num_ones = 0
            y = x

            while y > 0: 
                if y % 2:
                    num_ones += 1

                y = y // 2

            res.append(num_ones)
        
        return res
            