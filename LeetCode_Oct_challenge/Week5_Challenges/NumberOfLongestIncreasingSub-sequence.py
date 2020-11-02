'''
Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
'''


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        dp=[1]*len(nums)
        
        count=[1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if  nums[j]<nums[i]:
                    if dp[i]==dp[j]:
                        dp[i]=1+dp[j]
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
                        
        maxlength=max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == maxlength:
                res+=count[i]
        return res


obj = Solution()
res = obj.findNumberOfLIS([1,3,5,4,7])
print(res)