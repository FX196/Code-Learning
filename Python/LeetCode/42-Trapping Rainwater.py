class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        leftmax, rightmax = 0, 0
        while l < r:
            if leftmax < height[l]:
                leftmax = height[l]
            if rightmax < height[r]:
                rightmax = height[r]
            if leftmax > rightmax:
                ans += rightmax - height[r]
                r -= 1
            else:
                ans += leftmax - height[l]
                l += 1
        return ans
