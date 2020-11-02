'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or
all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
'''


class Solution:
    def minDominoRotations(self, A, B):
        s, n = set([1, 2, 3, 4, 5, 6]), len(A)
        for i in range(n):
            s &= set([A[i], B[i]])
        if not s:
            return -1
        flips1 = sum(A[i] == list(s)[0] for i in range(n))
        flips2 = sum(B[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2)


obj = Solution()
res = obj.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
print(res)
