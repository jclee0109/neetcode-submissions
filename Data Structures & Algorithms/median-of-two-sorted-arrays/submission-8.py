class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1, right1 = 0, len(nums1)-1
        left2, right2 = 0, len(nums2)-1

        if len(nums1) == 0:
            return (nums2[len(nums2)//2] + nums2[len(nums2)//2-1])/2 if len(nums2) % 2 == 0 else nums2[len(nums2)//2]
        if len(nums2) == 0:
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2 if len(nums1) % 2 == 0 else nums1[len(nums1)//2]
        i = 0
        while left1 <= right1 and left2 <= right2:

            mid1 = (left1+right1)//2
            mid2 = (left2+right2)//2
            
            if nums1[mid1] < nums2[mid2]:
                discard_cnt = min(mid1-left1, right2-mid2)
                if discard_cnt == 0:
                    arr = sorted(nums1[left1:right1+1] + nums2[left2:right2+1])
                    if (len(nums1)+len(nums2))%2 == 1:
                        return arr[len(arr)//2]
                    else:
                        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2

                left1 += discard_cnt
                right2 -= discard_cnt

            elif nums1[mid1] > nums2[mid2]:
                discard_cnt = min(right1-mid1, mid2-left2)
                if discard_cnt == 0:
                    arr = sorted(nums1[left1:right1+1] + nums2[left2:right2+1])
                    if (len(nums1)+len(nums2))%2 == 1:
                        return arr[len(arr)//2]  
                    else: 
                        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2

                right1 -= discard_cnt
                left2 += discard_cnt
                
            else: # 같으면 각각 양쪽 제거
                left1 = mid1
                right1 = (left1+right1+1)//2

                left2 = mid2
                right2 = (left2+right2+1)//2
                
                arr = sorted(nums1[left1:right1+1] + nums2[left2:right2+1])
                if (len(nums1)+len(nums2))%2 == 1:
                    return arr[len(arr)//2]  
                else: 
                    return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2


        
        return -1