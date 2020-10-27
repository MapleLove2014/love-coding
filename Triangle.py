class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle[-1])
        result = [[1 << 30] * n for _ in range(n)]
        result[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(n):
                if j >= len(triangle[i]):
                    continue
                if j == 0:
                    result[i][j] = result[i-1][j] + triangle[i][j]
                elif j == n-1:
                    result[i][j] = result[i-1][j-1] + triangle[i][j]
                else:
                    result[i][j] = min(result[i-1][j], result[i-1][j-1]) + triangle[i][j]
        return min(result[-1])
            
s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11)