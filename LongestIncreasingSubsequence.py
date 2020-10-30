class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dp = []
        for n in nums:
            if len(dp) == 0:
                dp.append(n)
            else:
                p = self.bs(dp, n)
                if p == len(dp):
                    dp.append(n)
                else:
                    dp[p] = n
        return len(dp)

    def bs(self, dp, n):
        low = 0
        high = len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid] == n:
                return mid
            if dp[mid] > n:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
        

s = Solution()
print(s.lengthOfLIS([0, 8, 4, 12, 2]))
print(s.lengthOfLIS([0, 8, 4, 12, 2]))