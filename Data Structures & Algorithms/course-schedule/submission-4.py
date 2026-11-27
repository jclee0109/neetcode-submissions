# bfs로 쭉 진행하면서 cycle 찾아야될듯
# 각 레벨에서 접근을 했는데, indegree가 남아있는 node가 있다? 뒤에서 들어오는거임.
# 각 레벨은 depth가 아니라 indegree가 1인 애들 기준으로 봄.
class Node:
    def __init__(self):
        self.child = []
        self.indegree = 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        available = []
        node_map = {}
        
        for second, first in prerequisites:
            node_map[first] = node_map.get(first, Node())
            node_map[second] = node_map.get(second, Node())
            node_map[second].indegree += 1
            
            node_map[first].child.append(node_map[second])
        
        for value, node in node_map.items():
            if node.indegree == 0:
                queue.append(node)

        num_free_courses = numCourses - len(node_map) # prerequisites 없는 과목들 = 전체과목 - 뭐라도 있는 애들

        cnt = 0
        while queue:
            node = queue.popleft()    
            cnt += 1
            if cnt + num_free_courses >= numCourses:
                return True

            for child in node.child:
                child.indegree -= 1
                if child.indegree == 0:
                    queue.append(child)

        
        return True if cnt+num_free_courses >= numCourses else False
        