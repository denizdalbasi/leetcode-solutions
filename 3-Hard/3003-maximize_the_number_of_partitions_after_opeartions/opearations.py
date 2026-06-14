class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        
        def dfs(i, mask, changed):
            state = (i, mask, changed)
            if state in memo:
                return memo[state]
            
            if i == n:
                return 1
            char_bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | char_bit
            
            if bin(new_mask).count('1') > k:
                res = 1 + dfs(i + 1, char_bit, changed)
            else:
                res = dfs(i + 1, new_mask, changed)
            if not changed:
                for d in range(26):
                    alt_mask = mask | (1 << d)
                    if bin(alt_mask).count('1') > k:
                        res = max(res, 1 + dfs(i + 1, 1 << d, True))
                    else:
                        res = max(res, dfs(i + 1, alt_mask, True))
                        
            memo[state] = res
            return res

        return dfs(0, 0, False)