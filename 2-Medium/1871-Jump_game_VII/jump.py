from collections import deque

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    if s[-1] == '1':
        return False
        
    n = len(s)
    queue = deque([0])
    far_reached = 0
    
    while queue:
        curr = queue.popleft()
        start = max(curr + minJump, far_reached + 1)
        end = min(curr + maxJump, n - 1)
        
        for j in range(start, end + 1):
            if s[j] == '0':
                if j == n - 1:
                    return True
                queue.append(j)
                
        far_reached = max(far_reached, end)
        
    return False