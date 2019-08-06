class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        num = len(M)
        visited = [False]*num
        count = 0
        
        def aCircle(student):
            for i in range(num):
                if not visited[i] and student[i]:
                    visited[i] = True
                    aCircle(M[i])
        
        for i in range(num):
            if not visited[i]:
                aCircle(M[i])
                count+=1
        return count