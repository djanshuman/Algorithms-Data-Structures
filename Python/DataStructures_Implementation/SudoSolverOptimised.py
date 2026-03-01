class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]
        emptyCell = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rowSet[r].add(val)
                    colSet[c].add(val)
                    boxSet[(r // 3) * 3 + c // 3].add(val)
                else:
                    emptyCell.append((r, c))

        def backTracker(idx):
            if idx == len(emptyCell):
                return True

            r, c = emptyCell[idx]
            block_idx = (r // 3 * 3) + c // 3

            for i in range(1, 10):
                val = str(i)
                if val not in rowSet[r] and val not in colSet[c] and val not in boxSet[block_idx]:
                    board[r][c] = val
                    rowSet[r].add(val)
                    colSet[c].add(val)
                    boxSet[block_idx].add(val)

                    if backTracker(idx + 1):
                        return True

                    board[r][c] = "."
                    rowSet[r].remove(val)
                    colSet[c].remove(val)
                    boxSet[block_idx].remove(val)

            return False

        backTracker(0)

# --- How to run locally for testing ---
if __name__ == "__main__":
    example_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    sol.solveSudoku(example_board)

    for row in example_board:
        print(row)
