class Solution:
    def minChanges(self, s: str) -> int:
        current_char = s[0]

        count = 0
        min_change = 0

        for char in s:
            if char == current_char:
                count += 1
                continue
            if count % 2 == 0:
                count = 1
            else:
                count = 0
                min_change += 1
            current_char = char
        return min_change