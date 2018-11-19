Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var findLength = function(A, B) {
  let res = 0;
  let arr = Array(A.length+1).fill(0).map(() => Array(B.length+1).fill(0));

  for(let i = A.length - 1; i >= 0; i--) {
    for(let j = B.length - 1; j >= 0; j--) {
      if(A[i] == B[j]) {
        arr[i][j] = arr[i+1][j+1] + 1;
        if(arr[i][j] > res) res = arr[i][j];
      }
    }
  }
  return res;
};
