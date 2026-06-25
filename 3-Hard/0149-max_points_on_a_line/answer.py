import math
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dy = y2 - y1
                dx = x2 - x1
                
                # Reduce fraction using GCD to handle precision and direction uniformly
                gcd = math.gcd(dy, dx)
                dy //= gcd
                dx //= gcd
                
                # Ensure a unique representation for lines (e.g., vertical/horizontal)
                if dx < 0 or (dx == 0 and dy < 0):
                    dy = -dy
                    dx = -dx
                
                slopes[(dy, dx)] += 1
            
            # The number of points on the line includes the anchor point (+1)
            current_max = max(slopes.values()) + 1 if slopes else 1
            max_points = max(max_points, current_max)
            
        return max_points