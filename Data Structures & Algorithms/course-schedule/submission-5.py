class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = {}
        indegree = [0]*numCourses

        for second, first in prerequisites:
            indegree[second] += 1
            edge[first] = edge.get(first, [])
            edge[first].append(second)

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            pre = queue.pop()
            if pre not in edge: # 마지막 노드는 저장이 안되어있을듯
                continue

            for post in edge[pre]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    queue.append(post)
            
        return True if sum(indegree) == 0 else False
