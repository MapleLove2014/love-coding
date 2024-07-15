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
    def merge2(self, intervals):
        # [[1,3], [2,6], [8,9]]
        result = []
        intervals=sorted(intervals, key=lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):  
            if intervals[i][0] <= end and intervals[i][1] >= start:
                end = max(intervals[i][1], end)
                start = min(intervals[i][0], start)
                continue
            
            result.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
        result.append([start, end])
        return result

s = Solution()
print(s.merge([[1,4],[0,0]]))