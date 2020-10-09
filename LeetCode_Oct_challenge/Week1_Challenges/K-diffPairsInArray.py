 """Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

 A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

         #0 <= i, j < nums.length
         #i != j
         #a <= b
         #b - a == k
 

 Example 1:

Input: nums = [3,1,4,1,5], k = 2
 Output: 2
 Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
 Although we have two 1s in the input, we should only return the number of unique pairs."""

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        d = {}
        count=0
        for n in nums:
            d[n]=d.get(n,0)+1
        for n in d:
            if k==0:
                if d[n] > 1:
                    count+=1
            else:
                if n+k in d:
                    count+=1
        return count

nums = list(map(int, input("Enter the array: ").strip().split()))
k = int(input("Enter the difference: "))
obj1 = Solution()
result = obj1.findPairs(nums, k)
print(result)