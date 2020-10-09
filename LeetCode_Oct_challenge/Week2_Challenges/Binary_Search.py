"""
Problem Statement: 
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Input:
nums = [-1,0,3,5,9,12], target = 9
Output:
4
Explanation:
9 exists in nums and its index is 4


Note:

1. You may assume that all elements in nums are unique.
2. n will be in the range [1, 10000].
3. The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums)
        if target>nums[r-1]:
            return -1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1

A = list(map(int, input().strip().split()))
target = int(input())

obj = Solution()
result = obj.search(A,target)
print(result)