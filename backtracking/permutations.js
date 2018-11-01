Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var permute = function(nums) {
  let res = [];
  dfs(nums, [], res);
  return res;
};

function dfs(nums, temp, res) {
  if(nums.length == temp.length) res.push(temp.slice(0));

  for(let i = 0; i < nums.length; i++) {
    if(temp.includes(nums[i])) continue;
    temp.push(nums[i]);
    dfs(nums, temp, res);
    temp.pop();
  }
}
