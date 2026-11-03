from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        queue = deque([(0, 0, grid[0][0])])
        
        visited = set()
        visited.add((0, 0, grid[0][0]))
        
        min_xor = float('inf')
        
        while queue:
            r, c, curr_xor = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                min_xor = min(min_xor, curr_xor)
                continue
            
            if r + 1 < m:
                next_xor = curr_xor ^ grid[r + 1][c]
                state = (r + 1, c, next_xor)
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
                    
            if c + 1 < n:
                next_xor = curr_xor ^ grid[r][c + 1]
                state = (r, c + 1, next_xor)
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
                    
        return min_xor