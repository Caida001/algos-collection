Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
 "adjacent" cells are those horizontally or vertically neighboring. The same
 letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */


var exist = function(board, word) {
  let w = board[0].length;
  let h = board.length;

  for(let i = 0; i < w; i++) {
    for(let j = 0; j < h; j++) {
      if(search(board, word, 0, i, j)) return true;
    }
  }
  return false;
};

function search(board, word, d, x, y) {
  if(x < 0 || y < 0 || x >= board[0].length || y >= board.length || word[d] != board[y][x]) return false;
  if(d == word.length -1) return true;
  let cur = board[y][x];
  board[y][x] = 0;
  let found = search(board, word, d+1, x+1, y) || search(board, word, d+1, x-1, y) || search(board, word, d+1, x, y+1) || search(board, word, d+1, x, y-1);
  board[y][x] = cur;
  return found;
}
