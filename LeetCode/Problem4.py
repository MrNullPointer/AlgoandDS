# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
#  Find the median of the two sorted arrays. The overall run time complexity sho
# uld be O(log (m+n)).
#
#  You may assume nums1 and nums2 cannot be both empty.
#
#  Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#  Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#  Related Topics Array Binary Search Divide and Conquer


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 1:
            return nums3[(len(nums3) // 2)]
        else:
            x = len(nums3) // 2
            return (nums3[x] + nums3[x - 1]) / 2

# leetcode submit region end(Prohibit modification and deletion)