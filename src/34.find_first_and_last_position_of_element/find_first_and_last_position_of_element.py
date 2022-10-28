from typing import List


# Time  -> O(n)
# Space -> O(1)
class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                while i + 1 < len(nums) and nums[i + 1] == target:
                    i += 1
                return [start, i]
        return [-1, -1]


class Solution2:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        start = self.search_start(nums, target)
        end = self.search_end(nums, target)
        return [start, end]

    def search_start(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == 0 or nums[middle - 1] != target:
                    return middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def search_end(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == (len(nums) - 1) or nums[middle + 1] != target:
                    return middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
