'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
'''


class Solution:
    def asteroidCollision(self, asteroids) -> list[int]:
        result = []
        for new in asteroids:
            while result and new < 0 < result[-1]:
                if result[-1] < -new:
                    result.pop()
                    continue
                elif result[-1] == -new:
                    result.pop()
                break
            else:
                result.append(new)
        return result

obj = Solution()
res = obj.asteroidCollision([5,10,-5])
print(res)