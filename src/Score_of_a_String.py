class Solution(object):
    def scoreOfString(self, s):
        res = 0
        left = 0
        right = 0

        for index in range(len(s) - 1):
            left = index
            right = index + 1
            charleft = s[left]  # fetching charac value at the index string
            charright = s[right]  # fetching charac value at the index string
            asil = ord(charleft)
            asir = ord(charright)
            # 10 =     3 + abs(101 - 108)  {7}
            res = res + abs(asil - asir)
            # print(f"Asciileft: {asil}")
            # print(f"Asciiright: {asir}, difPerIter {res}")

        return res

"""
## summary :
## problem  : 3110. Score of a String
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""