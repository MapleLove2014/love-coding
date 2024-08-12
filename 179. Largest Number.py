class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(nns, i, pivot):
            if nns[i] + pivot > pivot+nns[i]:
                return 1
            elif nns[i] + pivot == pivot+nns[i]:
                return 0
            return -1

        def part(nns, i, j):
            pivot = nns[i + (j - i) // 2]
            l = i - 1
            h = j + 1
            while True:
                l += 1
                while compare(nns, l, pivot) < 0:
                    l += 1
                h -= 1
                while compare(nns, h, pivot) > 0:
                    h -= 1
                if l >= h:
                    return h
                nns[l], nns[h] = nns[h], nns[l]

        def qsort(nns, i, j):
            if i < j:
                m = part(nns, i, j)
                qsort(nns, i, m)
                qsort(nns, m+1, j)
        
        nns = [str(num) for num in nums]
        if set(nns) == {'0'}:
            return '0'
        qsort(nns, 0, len(nns)-1)
        return "".join(reversed(nns))
s = Solution()
print(s.largestNumber([1,1,1]))



        


            
