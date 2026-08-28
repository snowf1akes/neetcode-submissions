class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i == ROWS or j < 0 or j == COLS or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i, j+1) #right
            dfs(i, j-1) #left
            dfs(i + 1, j) #up
            dfs(i - 1, j) #down 
                
        for m in range(ROWS):
            for n in range(COLS):
                if grid[m][n] == '1':
                    dfs(m, n)
                    count += 1
        return count