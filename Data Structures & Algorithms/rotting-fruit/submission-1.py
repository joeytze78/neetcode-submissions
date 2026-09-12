class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # no 2 in the grid, return -1
        # find the rotton fruit (2)
            # go to adjacent (left, right, up, down) 
                # if == 0 not doing anything
                # if == 1 change it to 2
                    # min += 1
            # loop until no more adjacent fruit is left unrotton 
            # assumption: only 1 rotton
        # [[2,1,1],
        # [0,1,1],
        # [1,0,1]]

        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            queue = deque()
            fresh = 0

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        queue.append((r,c))
                        visit.add((r,c))
                    elif grid[r][c] == 1:
                        fresh += 1

            minute = 0
            while queue and fresh>0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                                        
                    neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in neighbours:
                        if (min(r+dr,c+dc)<0 or
                            r+dr == ROWS or c+dc == COLS or
                            (r+dr,c+dc) in visit or 
                            grid[r+dr][c+dc] == 0):
                            continue

                        visit.add((r+dr,c+dc))
                        queue.append((r+dr, c+dc))
                        fresh -= 1
                minute += 1
            if fresh == 0: 
                return minute
            else: 
                return -1

        return bfs(grid)