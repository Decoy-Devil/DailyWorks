class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  # init dp

        for i in range(1, n + 1):  # loops for dp
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:  # if else fill for dp
                    dp[i][j] = dp[i - 1][j - 1] + 1  # diagonal + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # max(top, left)
        print(dp)
        L = dp[n][m]
        return n + m - 2 * L




'''Example 1: Input: word1 = "sea", word2 = "eat"
Output: 2 ~ Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2: Input: word1 = "leetcode", word2 = "etco"
Output: 4 '''

"""~~~~~~~~~~~~~~~~~~~~~~~~~ my code~~~
def min_steps_to_match(word1, word2):
    n = len(word1)
    m = len (word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # init dp



    for i in range(1, m+1): # loops for dp
        for j in range(1, n+1):
            if word1[i - 1] == word2[j - 1]:  # if else fill for dp
                dp[i][j] = dp[i - 1][j - 1] + 1  # diagonal + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # max(top, left)
    print(dp)
    L = dp[n][m]
    return n + m - 2 * L
    # here l is the matched part and 2 times l means we are deducing matching parts of both words
    # and counting the remaining steps and return

print(min_steps_to_match("eat", "tea"))

'''in Python, a string is already an indexable sequence
word1 = "eat"
print(word1[0])  # 'e'
print(word1[1])  # 'a'
print(word1[2])  # 't'
'''
# # R = 3)
# # C = 4
# # # tn = [[0 for _ in range(C)] for _ in range(R)]
# # # dp = [[0] * C] * R # wrong way to
# # print(dp)
#
# R = 2; C = 3
# dp = [[0]*C]*R
# dp[0][1] = 7
# print(dp)

"""

# words in python are already indexed word1[2] = "a"
# [0 for _ in range(something)] , means we want all the values inside the list to be 0 as number