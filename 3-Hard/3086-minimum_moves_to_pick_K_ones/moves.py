class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        pos = [i for i, x in enumerate(nums) if x == 1]
        n = len(pos)
        
        p_sum = [0] * (n + 1)
        for i, p in enumerate(pos):
            p_sum[i+1] = p_sum[i] + p
            
        ans = float('inf')
        
        min_existing = max(0, k - maxChanges)
        max_existing = min(k, n, min_existing + 3)
        
        for size in range(min_existing, max_existing + 1):
            rem = k - size
            
            base_cost = rem * 2
            
            if size == 0:
                ans = min(ans, base_cost)
                continue
                
            for i in range(n - size + 1):
                mid = i + size // 2
                
                left_count = mid - i
                right_count = (i + size - 1) - mid
                
                left_sum = p_sum[mid] - p_sum[i]
                right_sum = p_sum[i + size] - p_sum[mid + 1]
                
                cost = (pos[mid] * left_count - left_sum) + (right_sum - pos[mid] * right_count)
                
                ans = min(ans, cost + base_cost)
                
        return ans