class Solution:
    # https://medium.com/swlh/leetcode-largest-divisible-subset-93ab0860af85
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        dp = self.compute(sorted(nums))
        return self.retrieve(sorted(nums), dp)

    def retrieve(self, nums, dp):
        maxLen = max(dp)
        result = []
        pre = -1
        maxLenIndex = dp.index(maxLen)
        for i in range(maxLenIndex, -1, -1):
            if dp[i] == maxLen and (pre == -1 or result[-1] % nums[i] == 0):
                result.append(nums[i])
                maxLen -= 1
                pre = nums[i]
        return result


    def compute(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return dp

    def search(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        subsets = self.search(nums[1:])
        result = subsets.copy()
        hasYes = False
        for subset in subsets:
            if nums[0] % subset[-1] == 0:
                hasYes = True
                copySubset = subset.copy()
                copySubset.append(nums[0])
                result.append(copySubset)
        if not hasYes:
            result.append([nums[0]])
        return result



s = Solution()
print(s.largestDivisibleSubset([2,3,4,8]))
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4, 8]))
print(s.largestDivisibleSubset([3, 4, 16, 8]))
print(s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))

