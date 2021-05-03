class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda interval:interval[0])
        result = []
        preLeft = intervals[0][0]
        preRight = intervals[0][1]
        for interval in intervals:
            if interval[0]  <= preRight:
                preRight = max(interval[1], preRight)
                preLeft = min(interval[0], preLeft)
            else:
                result.append([preLeft, preRight])
                preLeft = interval[0]
                preRight = interval[1]
        result.append([preLeft, preRight])
        return result

s = Solution()
print(s.merge([[1,4],[0,0]]))