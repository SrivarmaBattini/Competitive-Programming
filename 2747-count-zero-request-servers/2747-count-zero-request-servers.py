class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        logs.sort(key = lambda a: a[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [0] * len(queries)
        active = {}
        right = left = 0

        for q, idx in sorted_queries:
            
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                active[server] = active.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                active[server] -= 1

                if active[server] == 0:
                    del active[server]

                left += 1

            res[idx] = n - len(active)
        
        return res