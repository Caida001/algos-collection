Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
  let res = [];
  if(n <= 0) return res;
  helper(res, "", n, n);
  return res;
};

function helper(res, s, left, right) {
  if(left > right) return;
  if(left == 0 && right == 0)  res.push(s);
  if(left > 0) helper(res, s+"(", left-1, right);
  if(right > 0) helper(res, s+")", left, right-1);
}
