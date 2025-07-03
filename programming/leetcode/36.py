from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
# following leetcoding guide on the bottom right
# create 9 hashsets for columns, 9 for rows and 9 for subgrids   
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    # determining subgrid will be tricky
    subgrids = [set() for _ in range(9)]

    # sudoku board is 9x9
    # ofc!!! i forgot about the special "." placeholder!
    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value == ".":
                continue
            subgrid_id = row // 3 * 3 + col // 3
            # [3,4] should be in id=4
            # [6,1] should be in id=6
            print(f"{value=} [{row},{col},{subgrid_id}]")
            if value in rows[row]:
                print("rows mismatch")
                return False
            if value in cols[col]:
                print("cols mismatch")
                return False
            if value in subgrids[subgrid_id]:
                print("subgrid mismatch")  # ofc subgrids are mismatched, ofc ahaha
                return False

            rows[row].add(value)
            cols[col].add(value)
            subgrids[subgrid_id].add(value)
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(board)