class Solution:
    def checkSubarraySum(self, nums, k):
        if not nums or len(nums) == 0:
            return False

        #sums = [[0] * len(nums) for _ in range(len(nums))]
        sums = [0] * len(nums)
        for i in range(len(nums)):
                if i == 0:
                    sums[i] = nums[i]
                else:
                    sums[i] = sums[i-1] + nums[i]

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                psum = sums[j] if i == 0 else sums[j] - sums[i-1]
                if k != 0 and psum % k == 0:
                    return True
                elif k == 0 and psum == 0:
                    return True
        return False

    def checkSubarraySumLinear(self, nums, k):
        if not nums or len(nums) == 0:
            return False

        sumsModK = {}
        sumsModK[0] = -1
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                sums = sums % k
            if sums in sumsModK:
                if i - sumsModK[sums] >= 2:
                    return True
            else:
                sumsModK[sums] = i

        return False

s = Solution()
print(s.checkSubarraySum([23, 2, 4, 6, 7], 6))
print(s.checkSubarraySum([23, 2, 4, 6, 7], 35))
print(s.checkSubarraySum([23, 2, 4, 6, 7], 88))
print(s.checkSubarraySum([23, 2, 4, 6, 7], -6))
print(s.checkSubarraySum([0, 0], 0))
print(s.checkSubarraySumLinear([0, 0], 0))


