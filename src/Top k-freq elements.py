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
