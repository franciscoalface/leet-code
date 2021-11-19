"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def add_binary(self, a: str, b: str):
        result = []
        carry = 0
        pos_a, pos_b = len(a) - 1, len(b) - 1
        while pos_a >= 0 or pos_b >= 0 or carry:
            total = carry

            if pos_a >= 0:
                total += int(a[pos_a])
                pos_a -= 1

            if pos_b >= 0:
                total += int(b[pos_b])
                pos_b -= 1

            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))
