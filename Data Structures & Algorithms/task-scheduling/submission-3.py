class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        available_task = []
        cooldown_task = []
        num_cnt = {}

        for task in tasks:
            num_cnt[task] = num_cnt.get(task, 0) + 1
        for task, cnt in num_cnt.items():
            heapq.heappush_max(available_task, (cnt, task))
        
        cycle_cnt = 0
        while available_task or cooldown_task:
            # print("cycle: ", cycle_cnt, available_task, cooldown_task)
            idle_flag = False
            while cooldown_task:
                cooldown, cnt, task = cooldown_task[0]
                if cooldown <= cycle_cnt:
                    heapq.heappop(cooldown_task)
                    heapq.heappush_max(available_task, (cnt, task))
                else: # idle 해야됨
                    idle_flag = True
                    break
            
            if not available_task and idle_flag:
                cycle_cnt += 1
                continue

            cnt, task = heapq.heappop_max(available_task)
            # print(task)
            
            if cnt > 1:
                heapq.heappush(cooldown_task, (cycle_cnt+n+1, cnt-1, task))
        
            cycle_cnt += 1
        
        return cycle_cnt