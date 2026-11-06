from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [0] * len(queries)
        server_counts = defaultdict(int)
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q, orig_index in indexed_queries:
            window_start = q - x
            window_end = q
            
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                server_counts[server_id] += 1
                right += 1
               
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1
                
            active_servers = len(server_counts)
            res[orig_index] = n - active_servers
            
        return res