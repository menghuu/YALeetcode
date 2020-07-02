class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        def bfs(i, j):
            assert grid[i][j] == '1'

            grid[i][j] = '#'
            deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in deltas:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == '1':
                        bfs(ni, nj)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        
        return ans
