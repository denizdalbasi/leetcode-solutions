from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)
            
            current_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (current_match and dfs(i + 1, j))
            
            if current_match:
                return dfs(i + 1, j + 1)
            
            return False

        return dfs(0, 0)