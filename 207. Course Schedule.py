class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        inDegree = [0] * numCourses
        inverseDependentRelation = [[] for _ in range(numCourses)]
        for p in prerequisites:
            course = p[0]
            pre = p[1]
            inDegree[course] += 1
            inverseDependentRelation[pre].append(course)
        stack = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            c = stack.pop()
            count += 1
            for postCourse in inverseDependentRelation[c]:
                inDegree[postCourse] -= 1
                if inDegree[postCourse] == 0:
                    stack.append(postCourse)
        return count == numCourses
        



    
s = Solution()
print(s.canFinish(2, [[1,0]]))
