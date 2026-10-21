class Solution:
    def minOperations(self, s: str) -> int:
        size = len(s)
        
        if all(s[i] <= s[i + 1] for i in range(size - 1)):
            return 0
            
        if size == 2:
            return -1
            
        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        # Check for strictly descending AFTER the 1-op check
        if all(s[i] >= s[i + 1] for i in range(size - 1)):
            return 3

        if mn in s[1:] or mx in s[:-1]:
            return 2
            
        return 3