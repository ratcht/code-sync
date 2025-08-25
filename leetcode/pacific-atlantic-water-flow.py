class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def bfs(starts: list):
            visited = set()
            queue = [*starts]
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            while queue:
                r, c = queue.pop(0)
                visited.add((r,c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        (nr,nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        # intersection: reachable from both oceans
        result = list(map(list, pacific_reachable & atlantic_reachable))

        return result