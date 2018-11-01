class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1
                end = len(nums) - 1

                while start < end:
                    if nums[i] + nums[start] + nums[end] == 0:
                        res.append([nums[i], nums[start], nums[end]])
                    if nums[i] + nums[start] + nums[end] < 0:
                        curStart = start
                        while start < end and nums[start] == nums[curStart]:
                            start += 1
                    else:
                        curEnd = end
                        while start < end and nums[end] == nums[curEnd]:
                            end -= 1
        return res


if __name__ == "__main__":
    result = Solution().threeSum([0, 0, 0])
    print(result)
