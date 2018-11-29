Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4



class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        """
        low = 0
        high = len(nums) - 1
        # Shuffle to avoid the worst case
        random.shuffle(nums)
        while low <= high:
            pIndex = self.partition(nums, low, high)
            if k < pIndex + 1:
                high = pIndex - 1
            elif k > pIndex + 1:
                low = pIndex + 1
            else:
                return nums[pIndex]


    def partition(self, nums, start, end):
      pIndex = start
      pivot = nums[end]
      for i in range(start, end):
        if nums[i] > pivot:
          nums[i], nums[pIndex] = nums[pIndex], nums[i]
          pIndex += 1
      nums[pIndex], nums[end] = nums[end], nums[pIndex]
      return pIndex
