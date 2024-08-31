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


    def productExceptSelf3(self, nums):
        
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suf[i] =  suf[i+1] * nums[i+1]
        ans = [1] * n
        for i in range(n):
            ans[i] = pre[i] * suf[i]
        return ans

    def productExceptSelf4(self, nums):
        
        n = len(nums)
        ans = [1] * n
        curr = 1
        for i in range(n):
            ans[i] *= curr
            curr *= nums[i]
        curr = 1
        for i in range(n-1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        return ans




s = Solution()
print(s.oneArray([1,2,3,4]))
print(s.productExceptSelf([0, 0]))