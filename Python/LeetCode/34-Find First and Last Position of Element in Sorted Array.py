class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # while not found
        low, high = 0, len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            return [-1, -1]
        i = j = mid
        while i >= 1 and nums[i - 1] == target:
            i -= 1
        while j <= len(nums) - 2 and nums[j + 1] == target:
            j += 1
        return [i, j]
