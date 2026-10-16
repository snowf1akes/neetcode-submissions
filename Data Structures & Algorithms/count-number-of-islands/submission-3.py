class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1 is land 0 is water
        #do a counter for islands maybe res = 0 at beginning 
        #go through the board, do dfs for the surround islands then sink them by turning 1 into 0, like if board[r][c] == "1": board[r][c] == '0' something like this? and at end of this dfs add count of islands += 1
        #then move onwards,

        #maybe at the end can do double for loop going from row, cols, applying this sinking island factor? 
        #at the very end after that double for loop, return res


    #intilization set res = 0, do a visited as a set 
        res = 0
        rows, cols = len(grid), len(grid[0])

    #dfs code here, bounds check min and max, also check if that val is already inside visited. since this dfs is only started when theres a 1 no need to check here, just assume its there. 
    #then do the sinking 
    
        def dfs(r, c,):
            #base cases bounds
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return 
            #sink current cell
            grid[r][c] = '0'

            #recurse dfs into 4 neighbours
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        #double for loop, maybe after each dfs run we can up the += 1 to res, and let dfs handle sinking only
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)

        #return res?  
        return res

















