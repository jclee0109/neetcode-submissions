class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_ans = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        return [x[0] for x in sorted_ans[:k]]
                