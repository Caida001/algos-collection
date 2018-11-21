Given n non-negative integers representing an elevation map where the width of
 each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


class Solution(object):
    def trap(self, height):
        a = 0
        b = len(height) - 1
        maximum = 0
        leftmax = 0
        rightmax = 0
        while a <= b:
          leftmax = max(leftmax, height[a])
          rightmax = max(rightmax, height[b])
          if leftmax < rightmax:
            maximum += leftmax - height[a]
            a += 1
          else:
            maximum += rightmax - height[b]
            b -= 1

        return maximum
