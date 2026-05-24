from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i: int, j: int) -> bool:
            # Base Case: If we reached the end of the pattern
            if j == len(p):
                # The match is only valid if we also consumed all of string s
                return i == len(s)
            
            # Check if the current characters match
            # (Careful not to go out of bounds on string s)
            current_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # If the next character in the pattern is a '*' wildcard
            if j + 1 < len(p) and p[j + 1] == '*':
                # Decision 1: Skip the '*' entirely (match 0 times)
                # Decision 2: Use the '*' (if current chars match, move i forward)
                return dfs(i, j + 2) or (current_match and dfs(i + 1, j))
            
            # If there is no '*' wildcard next, just move both pointers forward
            if current_match:
                return dfs(i + 1, j + 1)
            
            return False

        return dfs(0, 0)