class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        x = [0] * (n+1)
        k = 1
        results = []
        generateNQueens(x,k,n,results)
        return results


def isValid(x,k,l):
    for i in range(1,k):
        if (x[i] == l) or (abs(i-k) == abs(x[i] - l)):
            return False
    return True

def generateNQueens(x,k,n,results):
        for i in range (1,n+1):
            if isValid(x,k,i):
                x[k] = i
                if k == n:
                    board = []
                    for row in range(1,n+1):
                        line = "." * (x[row] -1) + "Q" + "." * (n- x[row])
                        board.append(line)
                    results.append(board)
                else:
                    generateNQueens(x, k + 1, n,results)

        x[k] = 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))


'''
[2, 4, 1, 3]
Row 1: Queen in column 2  →  . Q . .
Row 2: Queen in column 4  →  . . . Q
Row 3: Queen in column 1  →  Q . . .
Row 4: Queen in column 3  →  . . Q .
[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
'''


# LeetCode Version

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def isValid(k,l):
            for i in range(1,k):
                if (x[i] == l) or (abs(i-k) == abs(x[i] - l)):
                    return False
            return True

        def generateQueens(x,k,n,results):
            for i in range(1,n+1):
                if isValid(k,i):
                    x[k] = i

                    if k == n:
                        board = []
                        for row in range(1,n+1):
                            line = "." *(x[row] - 1) + "Q" + "." * (n - x[row])
                            board.append(line)
                        results.append(board)
                    else:
                        generateQueens(x,k+1,n,results)
            x[k] = 0
        

        x = [0] * (n+1)
        k=1
        results = []
        generateQueens(x,k,n,results)
        return results
