""" Remove Covered Intervals

 Solution
 Given a list of intervals, remove all intervals that are covered by another interval in the list.

 Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

 After doing so, return the number of remaining intervals."""

class Solution:
    def removeCoveredIntervals(self, intervals: list) -> int:
        intervals = sorted(intervals, key= lambda x: (x[0],-x[1]))
        count=0
        globalend = 0
        for _,end in intervals:
            if end>globalend:
                count+=1
                globalend = end
            
        return count



ob1 = Solution()
result = ob1.removeCoveredIntervals([[1,4],[3,6],[2,8]])
print(result)

