'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
'''


class Solution:
    def find132pattern(self, nums) -> bool:
        res = []
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if j < i-1:
                    res.append([nums[j], nums[i-1]])
                j = i
            for a in res:
                if nums[i] > a[0] and nums[i] < a[1]:
                    print(True)
            i += 1
        print(False)


obj = Solution()
obj.find132pattern([1, 2, 3, 4])