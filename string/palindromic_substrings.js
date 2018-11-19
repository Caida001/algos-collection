

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

let count = 1;
var countSubstrings = function(s) {
  if(s == null || s.length == 0) return 0;
  for(let i = 0; i < s.length-1; i++) {
    helper(s, i, i);
    helper(s, i, i+1);
  }
  return count;
};

function helper(s, left, right) {
  while(left >= 0 && right < s.length && s[left] === s[right]) {
    count++;
    left--;
    right++;
  }
}
