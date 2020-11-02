'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of
the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

'''


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in matrix:
            for j in i:
                if target == j:
                    print(True)
                if target < j:
                    print(False)


matrix = [[4, 5, 6], [4, 8, 9]]
tar = 9
obj = Solution()
obj.searchMatrix(matrix, tar)
