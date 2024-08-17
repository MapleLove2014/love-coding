import math
import time
class Solution:

    def countPrimes(self, n: int) -> int:
        def checkPrime(n):
            if n == 2:
                return True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        c = 0
        for i in range(2, n):
            if checkPrime(i):
                c += 1
        return c


    def countPrimes2(self, n: int) -> int:
        # https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Raji)/02%3A_Prime_Numbers/2.01%3A_The_Sieve_of_Eratosthenes
        p = [1] * (max(n, 2))
        p[0] = 0
        p[1] = 0
        i = 2
        while i ** 2 < n:
            if p[i] == 1:
                for j in range(i ** 2, n, i):
                    p[j] = 0
            i += 1
        return sum(p)
        

        
            
        
s = Solution()
s1 = int(time.time() * 1000)
print(s.countPrimes(100000))
s2 = int(time.time() * 1000)
print(s.countPrimes2(100000))
s3 = int(time.time() * 1000)
print("1:{},2:{}".format(s2 - s1, s3 - s2))
