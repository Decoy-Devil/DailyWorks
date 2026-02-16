"""
347 : Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]  # as array starts with 0

        # 1) count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # array.get(given default)

        print(count)

        # 2) bucket numbers by frequency
        for n, c in count.items():
            freq[c].append(n)

        print[freq]
        # 3) gather k results from highest freq to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):  # shows for loop for range allows 0 as end point, -1 for decemental
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     for n, c in count.items():
        #         freq[c].append(n)

        #     res = []
        #     for i in range(len(freq) -1, 0, -1):
        #     # shows for loop for range allows 0 as end point, -1 for decemental
        #         for n in freq[i]:
        #             res.append(n)
        #             if (len(res) == k):
        #                 return res
