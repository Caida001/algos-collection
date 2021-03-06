Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = self.helper(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
          return [-1, -1]

        return [left_idx, self.helper(nums, target, False)-1]




    def helper(self, nums, target, left):
        low = 0
        high = len(nums)

        while low < high:
          mid = (low + high) // 2
          if nums[mid] > target or (left and target == nums[mid]):
            high = mid
          else:
            low = mid+1
        return low
