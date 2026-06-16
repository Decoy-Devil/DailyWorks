"""Problem 1. [Category: Coding: Longest common subsequence] As discussed in Lecture slides, Longest
common subsequence problem gives you the task that given two strings x1x2...xm and y1y2...yn, find a
common subsequence that is as long as possible. The dynamic programming solution has been given in the
slides, your task here is to implement that in your favorite programming language.
Example 1:
Input:
2 7 5
2 5
Output: 2
Explanation: A common subsequence of length 2 is (2, 5)
Example 2:
Input:
2 7 8 3
5 2 8 7
Output: 2
Explanation: One common subsequence is (2, 7), another is (2, 8)"""



# Problem 1: Longest Common Subsequence

def longest_common_subsequence(A, B):
    # m stores the length of sequence A
    m = len(A)

    # n stores the length of sequence B
    n = len(B)

    # Create a DP table with (m + 1) rows and (n + 1) columns
    # Extra row and column are for the empty sequence case
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Loop through each element of A
    for i in range(1, m + 1):

        # Loop through each element of B
        for j in range(1, n + 1):

            # If current elements match, take diagonal value and add 1
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If current elements do not match, take maximum of top and left
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell contains the final LCS length
    return dp[m][n]


# Example 1
A = [2, 7, 5]
B = [2, 5]

print(longest_common_subsequence(A, B))


# Example 2
A = [2, 7, 8, 3]
B = [5, 2, 8, 7]

print(longest_common_subsequence(A, B))

