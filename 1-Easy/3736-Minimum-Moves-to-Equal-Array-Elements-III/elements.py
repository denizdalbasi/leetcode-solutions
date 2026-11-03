class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        total = 0

        for element in nums:
            total += (maximum - element)

        return total
        