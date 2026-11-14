class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #res number of islands + intialize board
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        #dfs here
        def dfs(r, c):
            #base cases
            #1. out of bounds, min and max
            #2. if grid[r][c] != '1'
            #return

            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0' #set 1 into 0 "sink the island"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c) ##sink the islands here 

        return res


