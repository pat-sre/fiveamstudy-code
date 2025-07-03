from typing import List 

def setZeroes1(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # following the 5 AM Leetcoding guide
    m = len(matrix)
    n = len(matrix[0])
    # if i see 0 at 0,0 i set x,0 and 0,x for all X to 0
    # i could store zeroed columns and rows?
    zeroed_rows = set()
    zeroed_cols = set()
    for row in range(m):
        for col in range(n):
            val = matrix[row][col]
            if val == 0:
                zeroed_cols.add(col)
                zeroed_rows.add(row)
    # now having all zeroed rows and cols we can zero them once and for all 
    # hmmm what about intersection of zeroed rows and cols T_T 
    # ok i know.

    print(zeroed_cols)
    print(zeroed_rows)
    # this zeroes only zeroes, not really what we lookin for
    for row in range(m):
        for col in range(n):
            if row in zeroed_rows and col in zeroed_cols:
                matrix[row][col] = 0

def setZeroes(matrix):
        m = len(matrix)
        n = len(matrix[0])
        first_col_has_zero = False
        first_row_has_zero = False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    print(row, col)
                    matrix[0][col] = 0
                    matrix[row][0] = 0
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if first_col_has_zero: # we have to zero 1st col
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row_has_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)