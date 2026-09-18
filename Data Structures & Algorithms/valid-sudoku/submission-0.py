class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hashset idea was right
        #unique method for 3x3 checking do row/3 and col/3 as key for position of 3x3
        #1. hashset for row, then check for dupes
        rows = collections.defaultdict(set)
        #2. hashset for cols, then check for dupes
        cols = collections.defaultdict(set)
        #3. 3x3 checking
        squares = collections.defaultdict(set) #key (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                #duplicate for rows quite a unqiue method imo
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True


