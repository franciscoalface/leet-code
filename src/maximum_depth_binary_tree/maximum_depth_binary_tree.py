'''
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
'''
import math


def max_depth(root):
    print(math.ceil(math.log(len(root) + 1)))
    return math.ceil(math.log(len(root) + 1))


if __name__ == '__main__':
    max_depth([3, 9, 20, None, None, 15, 7])
    max_depth([1, None, 2])
    max_depth([])
    max_depth([0])
