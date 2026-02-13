"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:
Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution(object):
    def isAnagram(self, s , t ):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dictionary_a = {}
        dictionary_b = {}

        for i in range(len(s)):
            # if key not in dictionary_a:
            #     dictionary_a[key] = 1
            # else:
            #     dictionary_a[key] = 1 + dictionary_a[key]
            # value = dictionary_a[key]
            dictionary_a[s[i]] = 1 + dictionary_a.get(s[i], 0)
    # -----
            # key = t[i]
            # if key not in dictionary_b:
            #     dictionary_b[key] = 1
            # else:
            #     dictionary_b[key] = 1 + dictionary_b[key]
            # value = dictionary_b[key]
            dictionary_b[t[i]] = 1 + dictionary_b.get(t[i], 0)
        return (dictionary_a == dictionary_b)
        
        
        