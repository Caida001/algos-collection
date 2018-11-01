Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
  if(!nums) return [];
  let res = [];
  helper(nums, [], 0, res);
  return res;
};

function helper(nums, temp, i, res) {
  res.push(temp.slice(0));
  for(i; i < nums.length; i++) {
    temp.push(nums[i]);
    helper(nums, temp, i+1, res);
    temp.pop();
  }
}
