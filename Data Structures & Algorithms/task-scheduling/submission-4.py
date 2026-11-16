class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 수식으로 풀기
        # max(실제 태스크 길이, (f-1)(n+1) + m) -> f: 가장 많이 등장한 횟수, m은 max_cnt가 같은 알파벳 개수
        cnt = [0]*26

        for task in tasks:
            cnt[ord(task) - ord("A")] += 1
        
        f = 0
        
        for task_cnt in cnt:
            f = max(f, task_cnt)
        
        m = 0
        for task_cnt in cnt:
            if task_cnt == f:
                m += 1
        
        return max(len(tasks), (f-1)*(n+1)+m)

