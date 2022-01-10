class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        if x <= 2:
            return 1


        start = 1
        end = x // 2

        while start <= end:
            mid = start + (end - start ) // 2
            product = mid * mid
            if product == x:
                return mid
            
            if product > x:
                end = mid - 1
            if product < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    start = mid + 1


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(3))
print(s.mySqrt(2147395599))
print(2147395599 - 46339 * 46339)
print(2147395599 - 46340 * 46340)



