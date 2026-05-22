class Solution:
    def rob(self, nums):
        # hint: if nums is empty -> return 0
        # hint: if nums has 1 element -> return that element
        n = len(nums)
        dp = [0] * n
        global max_val_rob
        max_val_rob = 0

        if(n == 0):
            return
        if(n == 1):
            return nums[0]
        if(n > 1):
            for i in range(len(n)):
                dp[i] = max(dp[i-1])

        pass


