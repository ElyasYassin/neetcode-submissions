class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))

            if heights[r] < heights[l]:
                r -= 1
            
            elif heights[l] < heights[r]:
                l += 1

            else:
                r -= 1
                l += 1
            
        return maxArea

            

