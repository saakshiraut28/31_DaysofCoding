'''
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
'''

import collections

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): 
            return False
        Count_A, Count_B = Counter(A), Counter(B)
        if Count_A != Count_B: 
            return False
        diff_places = sum([i!=j for i,j in zip(A,B)])
        if diff_places not in [0, 2]: 
            return False
        if diff_places == 0 and len(Count_A) == len(A): 
            return False
        if diff_places == 2 and len(Count_A) == 1: 
            return False
        return True
            

obj = Solution()
result = obj.buddyStrings("abcd","acbd")
print(result)