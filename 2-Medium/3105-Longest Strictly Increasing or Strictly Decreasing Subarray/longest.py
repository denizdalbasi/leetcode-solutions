class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = decreasing = longest = 1

        for index in range(len(nums) - 1):
            if nums[index + 1] > nums[index]:
                increasing += 1
                decreasing = 1
            elif nums[index + 1] < nums[index]:
                decreasing += 1
                increasing = 1
            else:
                increasing = decreasing = 1

            longest = max(longest, increasing, decreasing)

        return longest