class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        i=0 
        j=0
        ranges=[]
        while j < len(nums):
            _range = str(nums[i])
            while  j+1<len(nums) and nums[j+1]==nums[j]+1:
                j+=1
            if i!=j:
                _range += "->" + str(nums[j])
            ranges.append(_range)
            j+=1
            i=j
        return ranges


obj = Solution()
res = obj.summaryRanges([1,2,3,6,8,9])
print(res)

