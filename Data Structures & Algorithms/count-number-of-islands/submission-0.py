class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c, visit):
            if (min(r,c)<0 or
                r == ROWS or c == COLS):
                return
            if (r,c) not in visit and grid[r][c] == "1":
                visit.add((r,c))
                dfs(r-1, c, visit)
                dfs(r+1, c, visit)
                dfs(r, c+1, visit)
                dfs(r, c-1, visit)
                return

        visit = set()
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    count += 1
                    dfs(r, c, visit)
        
        return count 