class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        base = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        
        if ay1 >= by2 or by1 >= ay2 or ax1 >= bx2 or ax2 <= bx1:
            return base
        return base - (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1))
        
    
s = Solution()
print(s.computeArea(0, 0, 0, 0, -1, -1 , 1, 1))
