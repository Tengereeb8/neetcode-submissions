class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water = height * distance between the 2 bars
        maxWater = 0
        n = len(heights)

        l = 0
        r = n - 1

        #    l           r
        # [1,7,2,5,4,7,3,6]
        while l < r:
            currWater = min(heights[r], heights[l]) * (r - l)
            maxWater = max(maxWater, currWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater