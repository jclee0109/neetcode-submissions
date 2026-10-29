class TimeMap:
    # 자료구조 조금 더 간단하게 (굳이 num array가 아니어도 (set) array도 idx는 있으니 binary search 가능)
    def __init__(self):
        self.store = {}
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((timestamp, value))

        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left = 0
        right = len(values) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2
            time, value = values[mid]

            if time == timestamp:
                return value
            
            elif time < timestamp:
                ans = value
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

        
