class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # [3, 2, 3, 1, 3, 5, 3]
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        result = []
        for n in count:
            if count[n] > len(nums) // 3:

                result.append(n)
        return result

    def majorityElement2(self, nums):

        one = None
        two = None
        oneCount = 0
        twoCount = 0


        for n in nums:
            if one == None or one == n:
                one = n
                oneCount += 1
            elif two == None or two == n:
                two = n
                twoCount += 1
            elif oneCount == 0:
                one = n
                oneCount += 1
            elif twoCount == 0:
                two = n
                twoCount += 1
            else:
                oneCount -= 1
                twoCount -= 1 
        oneCount = 0
        twoCount = 0 
        for n in nums:
            if one == n:
                oneCount += 1
            if two == n:
                twoCount += 1

        result = []
        if oneCount > len(nums)//3:
            result.append(one)
        if twoCount > len(nums)//3:
            result.append(two)
        return result
