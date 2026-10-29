class TimeMap:

    def __init__(self):
        self.vocab = {}
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        default_obj = {timestamp:[]}

        obj = self.vocab.get(key, {}) # obj : timestamp & keys
        timestamp_arr = obj.get("timestamp", []) # Ascending ordered timestamp arr
        timestamp_arr.append(timestamp)
        obj["timestamp"] = timestamp_arr
        obj[timestamp] = value
        self.vocab[key] = obj
        return None

    def get(self, key: str, timestamp: int) -> str:
        try:
            obj = self.vocab[key]
        except KeyError as e:
            return ""
        
        timestamp_arr = obj.get("timestamp", [])

        if timestamp in obj:
            return obj[timestamp]

        left = 0
        right = len(timestamp_arr) - 1
        while left <= right:
            mid = (left+right)//2
            if right - left <= 1:
                if timestamp > timestamp_arr[right]:
                    return obj[timestamp_arr[right]]
                elif timestamp_arr[left] < timestamp:
                    return obj[timestamp_arr[left]]
                else:
                    return ""

            if timestamp_arr[mid] < timestamp:
                left = mid
            else:
                right = mid
        
        return -1

        
