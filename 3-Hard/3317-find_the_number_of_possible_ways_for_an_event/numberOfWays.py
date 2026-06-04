class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7
        max_k = min(n, x)
        
        S = [[0] * (max_k + 1) for _ in range(n + 1)]
        S[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, min(i, max_k) + 1):
                S[i][j] = (S[i-1][j-1] + j * S[i-1][j]) % MOD
                
        C = [0] * (max_k + 1)
        C[0] = 1
        curr_C = 1
        for i in range(1, max_k + 1):
            curr_C = (curr_C * (x - i + 1) * pow(i, MOD - 2, MOD)) % MOD
            C[i] = curr_C
            
        total_ways = 0
        factorial_i = 1
        pow_y_i = 1
        
        for i in range(1, max_k + 1):
            factorial_i = (factorial_i * i) % MOD
            pow_y_i = (pow_y_i * y) % MOD
            
            current_ways = (C[i] * S[n][i]) % MOD
            current_ways = (current_ways * factorial_i) % MOD
            current_ways = (current_ways * pow_y_i) % MOD
            
            total_ways = (total_ways + current_ways) % MOD
            
        return total_ways