class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_surface = 0

        while l < r:
            curr_surface = min(heights[l], heights[r]) * (r - l)
            max_surface = max(max_surface, curr_surface)
            
            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1

        return max_surface
            

        