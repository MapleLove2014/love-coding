class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        if i < 0:
            for x in range(j, -1, -1):
                nums1[k] = nums2[x]
                k-=1
        if j < 0:
            for y in range(i, -1 , -1):
                nums1[k] = nums1[y]
                k-=1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        invertIndex=m+n-1
        i1=m-1
        i2=n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] >= nums2[i2]:
                nums1[invertIndex] = nums1[i1]
                i1-=1
            else:
                nums1[invertIndex] = nums2[i2]
                i2-=1
            invertIndex -= 1
        while i2 >= 0:
            nums1[invertIndex] = nums2[i2]
            i2 -= 1
            invertIndex -= 1