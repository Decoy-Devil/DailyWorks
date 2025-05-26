class Solution(object):
    def romanToInt(self, s):
        # Initialize placeholders for characters and their numeric values
        cur_char   = None   # current Roman numeral character
        next_char  = None   # next Roman numeral character (for lookahead)
        cur_val    = 0      # integer value of cur_char
        next_val   = 0      # integer value of next_char
        result     = 0      # accumulator for the final result

        # Mapping from Roman numeral symbols (and a placeholder 'O') to integers
        roman_dict = {
            'O': 0,   # placeholder for positions beyond the end of the string
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0  # index to traverse the input string s
        # Loop until we've processed every character
        while i < len(s):
            cur_char  = s[i]                                            # fetch current character
            # fetch next character if it exists, otherwise use 'O' placeholder
            next_char = s[i+1] if (i + 1) < len(s) else 'O'
            cur_val   = roman_dict[cur_char]                            # lookup its value
            next_val  = roman_dict[next_char]                           # lookup lookahead value

            # If current value >= next value, it's additive notation
            if cur_val >= next_val:
                result += cur_val                                       # add normally
            else:
                # Subtractive notation (e.g. IV = 5 - 1)
                result += (next_val - cur_val)
                i += 1                                                  # skip the next char

            i += 1                                                      # advance to the next position

        return result  # return the final computed integer value

# ~~~~~~~~~~~ refactored code by gpt

"""class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to its integer value.
        Uses a single pass with lookahead: subtract if a smaller value precedes a larger one.
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        length = len(s)

        for i, ch in enumerate(s):
            value = roman_values[ch]
            # if next symbol is larger, this value should be subtracted
            if i + 1 < length and value < roman_values[s[i + 1]]:
                result -= value
            else:
                result += value

        return result"""

## problem  : 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].