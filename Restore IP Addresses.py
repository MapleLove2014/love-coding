class Solution:
    def restoreIpAddresses(self, s: str):
        

        def lookup(s, i, n, result, results):
            if i == len(s) and n == 0:
                results.append('.'.join([str(d) for d in result]))
                return
            if i == len(s):
                return
            for l in range(1, min(4, len(s) - i + 1)):
                left = len(s) - i - l
                if left < (n-1) or left > (n-1) * 3:
                    continue
                if l  == 1:
                    # 选一个元素
                    lookup(s, i+l, n-1, result + [int(s[i])], results)
                elif s[i] != '0' and int(s[i:i+l]) <= 255:
                    lookup(s, i+l, n-1, result + [int(s[i:i+l])], results)
        results = []
        lookup(s, 0, 4, [], results)
        return results

s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("0000"))