class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        return str(x) == str(x)[::-1]

    def optimized(self, x):
        if x < 0 :
            return False
        if x < 10:
            return True
        if x > 0 and x % 10 == 0:
            return False
        
        reversedHalf = 0
        while x > reversedHalf:
            reversedHalf = reversedHalf * 10 + x % 10
            x //= 10
        
        return x == reversedHalf or x == reversedHalf // 10


s = Solution()
print(s.isPalindrome(121) == True)
print(s.isPalindrome(123) == False)