class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # deque로 풀기 (어차피 cycle + n + 1은 단조증가, FIFO로도 가능)
        available = []
        cooldown = deque()

        # available: max heap (cnt, task)
        # cooldown: queue

        task_cnt = {}
        for task in tasks:
            task_cnt[task] = task_cnt.get(task, 0) + 1

        # available에 모두 채우기
        for task, cnt in task_cnt.items():
            heapq.heappush_max(available, (cnt, task))

        cycle = 0
        while available or cooldown:
            while cooldown:
                next_cycle, cnt, task = cooldown[0]
                if cycle >= next_cycle:
                    cooldown.popleft()
                    heapq.heappush_max(available, (cnt, task))
                elif available:
                    break
                else:
                    cycle = next_cycle

            # heap에서 빼고
            cnt, task = heapq.heappop_max(available)
            if cnt > 1:
                # cooldown에 새로 채워넣기
                cooldown.append((cycle+n+1, cnt-1, task))
            cycle += 1
            
        
        return cycle
