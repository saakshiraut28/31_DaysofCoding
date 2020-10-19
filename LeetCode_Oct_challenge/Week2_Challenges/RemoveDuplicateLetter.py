'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:

Input: s = "bcabc"
Output: "abc"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        reverse_str_set = {c: i for i,c in enumerate(s)}
        result_string = ["!"]
        avoid_dup = set()
        
        for i,letter in enumerate(s):
            if letter in avoid_dup:
                continue
            else:
                while(letter < result_string[-1] and reverse_str_set[result_string[-1]] > i):
                    avoid_dup.remove(result_string.pop())
                
                result_string.append(letter)
                avoid_dup.add(letter)
                
        final_str = "".join(result_string)[1:]
        return final_str


obj = Solution()
result_string = obj.removeDuplicateLetters("abcccdcd")
print(result_string)