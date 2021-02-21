class Solution:
    def numberOfArithmeticSlices(self, A):
        if not A or len(A) < 3:
            return 0
        dp = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4]) == 3)

        