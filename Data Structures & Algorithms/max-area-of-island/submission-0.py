class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r,c)<0 or
                r == ROWS or c == COLS or
                (r,c) in visit or 
                grid[r][c] == 0):
                return 0
            
            visit.add((r,c))
            count = 1
            count += dfs(r+1, c, visit)
            count += dfs(r-1, c, visit)
            count += dfs(r, c+1, visit)
            count += dfs(r, c-1, visit)
            return count
            
        visit = set()
        count = 0
        most_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visit:
                    count = dfs(r, c, visit)
                    if count > most_count:
                        most_count = count
                    else:
                        count = 0
        
        return most_count