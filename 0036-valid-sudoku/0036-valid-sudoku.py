from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit == '.':
                    continue
                sq_id = (r // 3) * 3 + (c // 3) 
                if digit in rows[r] or digit in cols[c] or digit in sq[sq_id]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                sq[sq_id].add(digit)
        
        return True