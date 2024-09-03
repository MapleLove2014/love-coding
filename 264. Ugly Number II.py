class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        p = [2,3,5]
        nexts = [2,3,5]
        inc = [0] * 3
        while len(ans) < n:
            u = min(nexts)
            ans.append(u)
            for i in range(3):
                if nexts[i] == u:
                    inc[i] += 1
                    nexts[i] = p[i] * ans[inc[i]]
        return ans[-1]
    

s = Solution()
print(s.nthUglyNumber(10))

            





