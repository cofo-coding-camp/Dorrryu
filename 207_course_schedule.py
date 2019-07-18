class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses
        done = [[] for _ in range(numCourses)]
        
        
        for course, pre in prerequisites:
            done[course].append(pre)

        for course in range(len(done)):
            if not self.dfs(visited, course, done):
                return False
        return True
    
    def dfs(self, visited, course, done):
        if visited[course] == 1:
            return True
        elif visited[course] == -1:
            return False
        visited[course] = -1
        for pre in done[course]:
            if not self.dfs(visited, pre, done):
                return False
        visited[course] = 1
        return True