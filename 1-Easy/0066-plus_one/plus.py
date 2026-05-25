class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] >= 10:
            digits[i] = 0
            i -= 1
            if i < 0:
                break
            digits[i] += 1
        if i < 0:
            return [1] + digits
        return digits