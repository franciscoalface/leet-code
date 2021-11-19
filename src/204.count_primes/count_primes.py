"""
Given an integer n, return the number of prime numbers
that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 10**6
"""
import math


class Solution:
    def count_primes(self, num: int) -> int:
        if num < 2:
            return 0

        is_prime = [True] * num
        # 0 and 1 are not primes
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(num)))):
            if is_prime[i]:
                for multiples_of_i in range(i * i, num, i):
                    is_prime[multiples_of_i] = False
        return sum(is_prime)
