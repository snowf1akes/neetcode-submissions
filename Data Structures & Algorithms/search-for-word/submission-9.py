class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r , c, i):
            #base case that we found end of the word?
            if i == len(word):
                return True

            #rejection reasons. 
            #bounds min and max
            #already visited node / path
            #word[i] != board[r][c] not in board
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in path or word[i] != board[r][c]:
                return False

            #after those recursive checks above, add in the (r, c) into path
            path.add((r,c))
            #where do i backtrack?!?
            #do the actual dfs part now
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r,c)) #backtrack after dfs hasn't found shit
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r , c, 0): 
                    return True
        return False

