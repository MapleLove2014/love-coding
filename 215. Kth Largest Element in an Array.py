class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def qs(nums, i, j):
            
            l = i - 1
            h = j + 1
            mid = i + (j - i) // 2
            pivot = nums[mid]
            while True:
                l += 1
                while nums[l] < pivot:
                    l += 1
                h -= 1
                while nums[h] > pivot:
                    h -= 1
                if l < h:
                    nums[l], nums[h] = nums[h], nums[l]
                else:
                    return h
        def qsw(nums, i, j, k):
            if i < j:
                index = qs(nums, i, j)
                kth = len(nums) - k
                if index >= kth:
                    qsw(nums, i, index, k)
                else:
                    qsw(nums, index + 1, j, k)
        qsw(nums, 0, len(nums) - 1, k)
        return nums[len(nums)-k]
    

    def findKthLargest2(self, nums: list[int], k: int) -> int:

        pq = [2**31]
        def size(pq):
            return len(pq) - 1
        def insert(pq, n):
            pq.append(n)
            s = size(pq)
            while pq[s // 2] < n:
                pq[s // 2], pq[s] = pq[s], pq[s // 2]
                s = s // 2
        def pop(pq):
            if size(pq) == 0:
                return None
            last = pq.pop()
            if size(pq) == 0:
                return last
            e = pq[1]
            i = 1
            pq[i] = last
            s = size(pq)
            while 2*i <= s:
                pos = (2*i + 1) if 2*i + 1 <= s and pq[2*i+1] > pq[2*i] else 2*i
                if pq[pos] > pq[i]:
                    pq[pos], pq[i] = pq[i], pq[pos]
                    i = pos
                else:
                    break
            return e
        for n in nums:
            insert(pq, n)
        print(pq)
        for _ in range(k-1):
            pop(pq)

        return pop(pq)

s = Solution()
print(s.findKthLargest2([3,2,1,5,6,4], 2))
print(s.findKthLargest2([3,2,3,1,2,4,5,5,6], 4))
print(s.findKthLargest2([3], 1))



