You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function addTwoNumbers(l1, l2) {
  let str1 = "";
  let str2 = "";
  while(l1.next != null) {
    str1 += l1.val;
    l1 = l1.next;
  }
  while(l2.next != null) {
    str2 += l2.val;
    l2 = l2.next;
  }
  str1 += l1.val;
  str2 += l2.val;
  str1 = str1.split("").reverse().join("");
  str2 = str2.split("").reverse().join("");

  let num = parseInt(str1) + parseInt(str2);
  num = num.toString().split("").reverse();

  let list = new ListNode(0);
  let res = list;
  for(let i = 0; i < num.length; i++){
    list.next = new ListNode(parseInt(num[i]));
    list = list.next;
  }
  return res.next;
}
