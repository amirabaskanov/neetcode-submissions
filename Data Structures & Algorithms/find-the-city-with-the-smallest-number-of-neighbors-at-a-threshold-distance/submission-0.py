class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        city_map = defaultdict(list)
        for city1, city2, dist in edges:
            city_map[city1].append([city2, dist])
            city_map[city2].append([city1, dist])

        def dijkstra(src):
            heap = [(0, src)] # dist, node
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in city_map[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            return len(visit) -1
        
        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count
        return res