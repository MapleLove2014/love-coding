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
    
    def majorityElement3(self, nums):
        
        the = len(nums)//3
        can1 = None
        can2 = None
        c1 = 0
        c2 = 0

        for n in nums:
            if c1 == 0 and n != can2:
                can1 = n
                c1 = 1
            elif c2 == 0 and n != can1:
                can2 = n
                c2 = 1
            elif c1 != 0 and n == can1:
                c1 += 1
            elif c2 != 0 and n == can2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
            if c1 == 0:
                can1 = None
            if c2 == 0:
                can2 = None

        c1 = 0
        c2 = 0
        for n in nums:
            if n == can1:
                c1 += 1
            if n == can2:
                c2 += 1
        

        ans = []
        if c1 > the:
            ans.append(can1)
        if c2 > the and can1 != can2:
            ans.append(can2)
        return ans

