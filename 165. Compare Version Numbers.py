class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        vv1 = [int(k) for k in v1] + [0]*max(0, len(v2)-len(v1))
        vv2 = [int(k) for k in v2] + [0]*max(0, len(v1)-len(v2))
        for i in range(len(vv1)):
            if vv1[i] > vv2[i]:
                return 1
            if vv1[i] < vv2[i]:
                return -1
        return 0

s = Solution()
print(s.compareVersion("1.0.1", "1"))
                