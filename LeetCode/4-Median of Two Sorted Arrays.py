class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if nums1 or nums2:
            nums = sorted(list(nums1) + list(nums2))
            length = len(nums)
            if (length % 2 == 0):
                return (nums[int(length / 2 - 1)] + nums[int(length / 2)]) / 2
            else:
                return nums[int((length + 1) / 2) - 1]
        else:
            return 0
