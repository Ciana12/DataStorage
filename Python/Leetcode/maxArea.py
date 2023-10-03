class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between the two lines
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area