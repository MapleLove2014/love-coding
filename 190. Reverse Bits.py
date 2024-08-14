def printb(n):
    print('0b{0: >32}'.format(bin(n)[2:].rjust(32, '0')))


class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0xffffffff
        for i in range(16):
            lo = 1 << i
            l = n & lo
            ho = 1 << (32 - i - 1)
            h = n & ho                 
            n = (n & (lo ^ mask)) | (h >> (32 - i - 1 -i))
            n = (n & (ho ^ mask)) | (l << (32 - i - 1 -i))
        return n
    

s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))




