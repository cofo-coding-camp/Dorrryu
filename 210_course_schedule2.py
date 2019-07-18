class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = [0] * numCourses
        pres = [[] for _ in range(numCourses)]
        self.res = []
        
        for course, pre in prerequisites:
            pres[course].append(pre)
        
        for course in range(numCourses):
            if not self.dfs(course, pres, visit):
                return []
        return self.res
            
            
    def dfs(self, course, pres, visit):
        if visit[course] == 1:
            return True 
        elif visit[course] == -1:
            return False
        visit[course] = -1
        for pre in pres[course]:
            if not self.dfs(pre, pres, visit):
                return False
        visit[course] = 1
        self.res.append(course)
        return True