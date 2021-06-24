/*
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
  3
 / \
9  20
  /  \
 15   7
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
*/

function maxDepth(root) {
	return Math.ceil(Math.log2(root.length + 1));
}

module.exports = maxDepth;

console.log(maxDepth([3, 9, 20, null, null, 15, 7]));
console.log(maxDepth([1, null, 2]));
console.log(maxDepth([]));
console.log(maxDepth([0]));
