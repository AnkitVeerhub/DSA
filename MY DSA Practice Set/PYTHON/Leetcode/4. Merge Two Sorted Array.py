'''
Merge Two Sorted Array
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
# Bruteforce but not recommended
def merge_two_sorted_array(nums1,nums2):
    result = nums1 + nums2
    result.sort()
    return result
nums1,nums2 = [1,3], [2]
print(merge_two_sorted_array(nums1, nums2))

# Bruteforce recommended
def merge_two_sorted_array(nums1,nums2):
    result = []
    i, j = 0, 0
    while(i < len(nums1) and j < len(nums2)):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    while(i < len(nums1)):
        result.append(nums1[i])
        i += 1
    while(j < len(nums2)):
        result.append(nums2[j])
        j += 1
    return result
def find_median(nums1, nums2):
    merged = merge_two_sorted_array(nums1, nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 1:
        return float(merged[mid])
    else:
        return (merged[mid - 1] + merged[mid])/2.0
nums1,nums2 = [1,3], [2]
print(merge_two_sorted_array(nums1, nums2))
print(find_median(nums1, nums2))