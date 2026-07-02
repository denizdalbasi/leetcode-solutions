from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        max_health_at = [[-1] * n for _ in range(m)]
        
        start_health = health - grid[0][0]
        
        if start_health <= 0:
            return False
            
        max_health_at[0][0] = start_health
        
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            current_health = max_health_at[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_health = current_health - grid[nr][nc]
                    
                    if next_health > 0 and next_health > max_health_at[nr][nc]:
                        max_health_at[nr][nc] = next_health
                        queue.append((nr, nc))
        
        return max_health_at[m - 1][n - 1] >= 1