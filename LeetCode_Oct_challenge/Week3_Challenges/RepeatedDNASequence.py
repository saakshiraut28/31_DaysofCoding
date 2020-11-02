'''
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G',
and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful
to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        unique = set()
        result = set()
        for i in range(len(s)-9):
            active = s[i:i+10]
            if active in unique:
                result.add(active)
            unique.add(active)
        return [*result]


obj = Solution()
res = obj.findRepeatedDnaSequences("AAAAACCCCCAAAAAACCCCCGGGGTTTT")
print(res)
