class Solution:
    def productExceptSelf(self, nums):
        
        """
            0,0
        """

        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        
        pre = 1
        post = 1
        for i in range(len(nums)):
            pre *= nums[i]
            prefix[i] = pre

            post *= nums[len(nums)-1 - i]
            postfix[len(nums)-1 -i] = post
        print(prefix)
        print(postfix)
        result = [1]*len(nums)
        for i in range(len(nums)):
            prei = i - 1
            posti = i + 1
            if prei >= 0:
                result[i] *= prefix[prei]
            if posti < len(nums):
                result[i] *= postfix[posti] 
        return result

    def oneArray(self, nums):


        temp = 1
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = temp * result[i]
            temp *= nums[i]
        return result




s = Solution()
print(s.oneArray([1,2,3,4]))
print(s.productExceptSelf([0, 0]))