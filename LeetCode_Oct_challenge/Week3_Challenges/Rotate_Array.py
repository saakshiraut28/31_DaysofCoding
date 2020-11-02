'''
Given an array, rotate the array to the right by k steps, where k is
non-negative.
Follow up:

Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:

rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def inverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        k = k % n
        inverse(0, n-1)
        inverse(0, k-1)
        inverse(k, n-1)
        print(nums)


nums = [1, 2, 3, 6, 9, 4, 5]
obj = Solution()
obj.rotate(nums, 5)
