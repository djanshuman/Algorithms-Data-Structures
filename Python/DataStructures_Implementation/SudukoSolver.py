def isValid(r, c, val):
    # Check same row , val not present
    for i in range(9):
        if mat[r][i] == val:
            return False

    # Check same column , val not present
    for i in range(9):
        if mat[i][c] == val:
            return False

    rowBound = r - r%3
    colBound = c - c%3

    for i in range(0,3):
        for j in range(0,3):
            if mat[rowBound +i][colBound +j] == val:
                return False
    return True

def sudukoSolver(mat,r,c):
    # Check Base case when we have exhaused till last row & column
    if r == 8 and c == 9:
        return True
    # Check if we are in last row & column
    if c == 9:
        r += 1
        c = 0

    if mat[r][c] != 0:
        return sudukoSolver(mat,r,c+1)

    # Enter matrix to fill values
    for i in range(1,10):
        if isValid(r,c,i):
            mat[r][c] = i
            if sudukoSolver(mat,r,c+1):
                return True
            mat[r][c] = 0
    return False
if __name__ == "__main__":
    mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    r , c = 0,0
    sudukoSolver(mat,r,c)
    for i in mat:
        print(i)
