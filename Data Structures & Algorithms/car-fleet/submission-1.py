class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idx_stack = []
        ans = 0
        
        cars = sorted(zip(position, speed), key=lambda x: x[0])

        for i in range(len(cars)):
            car_current = cars[i]
            t_current = (target - car_current[0])/car_current[1]
            
            while len(idx_stack) > 0:
                prev = idx_stack[-1]
                car_prev = cars[prev]
                t_prev = (target - car_prev[0])/car_prev[1]
                if t_prev <= t_current: # 이전 차가 나보다 빠름 -> 합쳐짐
                    idx_stack.pop()
                else:
                    break
   
            idx_stack.append(i)


        return len(idx_stack)



        