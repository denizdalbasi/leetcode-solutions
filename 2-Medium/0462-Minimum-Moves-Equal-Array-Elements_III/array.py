class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        middle = nums[int(len(nums) /2)]
        total = 0
        for element in nums:
            total += abs(middle-element)

        return total
            
        