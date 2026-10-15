class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [height[0]]
        maxRight = [height[-1]]

        for x in height[1:]:
            if x > maxLeft[-1]:
                maxLeft.append(x)
            else:
                maxLeft.append(maxLeft[-1])

        for y in height[-2::-1]:
            if y > maxRight[-1]:
                maxRight.append(y)
            else:
                maxRight.append(maxRight[-1])

        maxRight = maxRight[::-1]
            
        min_lr = [min(maxLeft[i], maxRight[i]) for i in range(len(height))]

        res = 0

        for n in range(len(min_lr)):
            res += max(0, min_lr[n] - height[n])

      
        return res
