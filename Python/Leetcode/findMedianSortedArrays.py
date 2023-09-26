class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            # Ensure nums1 is the smaller array to simplify the implementation
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        median = 0
        
        while left <= right:
            partition1 = (left + right) // 2  # Partition index for nums1
            partition2 = (m + n + 1) // 2 - partition1  # Partition index for nums2
            
            # Calculate the maximum and minimum values on the left and right sides of the partitions
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Valid partition found, calculate the median
                if (m + n) % 2 == 0:
                    median = (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    median = max(max_left1, max_left2)
                break
            elif max_left1 > min_right2:
                # Partition is too far to the left, move the partition to the left in nums1
                right = partition1 - 1
            else:
                # Partition is too far to the right, move the partition to the right in nums1
                left = partition1 + 1
        
        return median