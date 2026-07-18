"""Problem 2. [Category: Coding: Word segmentation]
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = “catdog”, wordDict = [“cat”,“dog”]
Output: true
Explanation: Return true because “catdog” can be segmented as “cat dog”.
Example 2:
Input: s = “applepenapple”, wordDict = [“apple”,“pen”]
Output: true
Explanation: Return true because “applepenapple” can be segmented as “apple pen apple”.
Note that you are allowed to reuse a dictionary word."""
# Problem 2: Word Segmentation

def word_break(s, wordDict):
    # Convert wordDict into a set for faster lookup
    word_set = set(wordDict)

    # n stores the length of the input string
    n = len(s)

    # Create a DP array of size n + 1
    # dp[i] means whether first i characters can be segmented
    dp = [False] * (n + 1)

    # Empty string can always be segmented
    dp[0] = True

    # Loop through every ending position i
    for i in range(1, n + 1):

        # Try every possible split position j before i
        for j in range(0, i):

            # Check if left part is valid and right part is in dictionary
            if dp[j] == True and s[j:i] in word_set:

                # Mark first i characters as segmentable
                dp[i] = True

                # No need to check more splits for this i
                break

    # Final answer tells whether full string can be segmented
    return dp[n]


# Example 1
s = "catdog"
wordDict = ["cat", "dog"]

print(word_break(s, wordDict))


# Example 2
s = "applepenapple"
wordDict = ["apple", "pen"]

print(word_break(s, wordDict))

