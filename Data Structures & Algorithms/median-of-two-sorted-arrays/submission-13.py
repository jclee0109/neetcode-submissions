class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 이진탐색을 nums1 (A) 에 들어갈 개수(i)를 찾는걸로 정의
        # 꼭 A가 아니더라도 min(len(nums1), len(nums2))로 정하면 좋을 듯
        # 0 <= i < len(nums1 or nums2)
        # i가 정해지면 j = 길이//2 - i

        # i를 나눴으면 (i+j == (len(nums1) + len(nums2)) // 2)
        # A의 모든 왼쪽 파티션에 들어갈 내용들 (i) | A의 오른쪽 파티션
        # B의 모든 왼쪽 파티션에 들어갈 내용들 (j) | B의 오른쪽 파티션

        # left(B)의 max (마지막 원소 j-1) <= right(A)의 min(첫번째 원소 i)
        # left(A)의 max (마지막 원소 i-1) <= right(B)의 min(첫번째 원소 j)

        A = nums1
        B = nums2

        if len(nums1) > len(nums2):
            A = nums2
            B = nums1

        total = len(A) + len(B)    
        i_min = 0
        i_max = len(A)

        while i_min <= i_max:
            i = (i_min+i_max)//2
            j = (total)//2 - i
            # 만족하는지 2conditions check (동시에 만족할 수는 없음)
            # 조건1 (max(left(B)) <= min(right(A)))

            left_A_max = A[i-1] if i>0 else -float('inf')
            left_B_max = B[j-1] if j>0 else -float('inf')

            right_A_min = A[i] if 0<len(A) and i < len(A) else float('inf')
            right_B_min = B[j] if j < len(B) else float('inf')

            # 만족하지 않으면 i가 부족한거임 (left를 i+1로)
            if left_B_max > right_A_min:
                i_min = i+1
                continue

            # 조건2
            # 만족하지 않으면 i가 많은거임 (right를 i-1로)
            elif left_A_max > right_B_min:
                i_max = i-1
                continue 

            # 둘다 만족하면
            # break 하고 정답 출력
            else:
                left_max = max(left_A_max, left_B_max)
                right_min = min(right_A_min, right_B_min)

                if total % 2 == 1:
                    return max(left_max, right_min)
                else:
                    return (left_max+right_min)/2

        reutn -1

            
        