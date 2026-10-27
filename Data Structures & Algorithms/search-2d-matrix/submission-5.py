class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row candidate (log(n)) binary search
        left, right = 0, len(matrix) - 1
        candidate = -1
        flag = False

        while left <= right:
            mid = (right + left) // 2
            mid_first = matrix[mid][0]
            mid_last = matrix[mid][-1]
            if mid_first == target or mid_last == target:
                return True
            
            if mid_first < target and target < mid_last:
                row = mid
                flag = True
                break
            elif mid_first > target:
                right = mid - 1
            elif mid_last < target:
                left = mid + 1
        
        if not flag:
            return False
        
        # find target in the row (log(m)) -> log(n) + log(m) = log(mn)
        row_arr = matrix[row]

        left, right = 0, len(row_arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if row_arr[mid] == target:
                return True
            elif row_arr[mid] < target:
                left = mid+1
            elif row_arr[mid] > target:
                right = mid-1
        
        return False

        
