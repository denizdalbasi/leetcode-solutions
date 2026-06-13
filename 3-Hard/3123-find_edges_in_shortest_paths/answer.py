import heapq

class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))
            
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)] # (dist, u)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w, idx in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
        ans = [False] * len(edges)
        if dist[n - 1] == float('inf'):
            return ans
            
        # Backtrack from n-1 to 0 using DFS/BFS to mark edges
        visited = [False] * n
        def dfs(u):
            if u == 0:
                return
            visited[u] = True
            for v, w, idx in adj[u]:
                if dist[u] == dist[v] + w:
                    ans[idx] = True
                    if not visited[v]:
                        dfs(v)
                        
        dfs(n - 1)
        return ans