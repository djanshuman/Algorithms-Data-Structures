'''
https://leetcode.com/problems/search-a-2d-matrix/description/
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while (top <= bottom):
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -= 1
            else:
                break
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        l = 0
        r = cols - 1

        while( l <= r):
            mid = (l+r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
