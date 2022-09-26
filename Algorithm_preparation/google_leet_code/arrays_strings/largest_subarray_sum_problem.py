from typing import List

import math


class Solution:

    def largestSubarraySum(self, nums: List[int]) -> int:

        negative_infinity = -math.inf
        maximum_sum_so_far = nums[0]

        left_pointer = 0
        right_pointer = 1
        sum_so_far = 0

        for i in range(0, len(nums)):

            # At every step we have two options either take that index into account or drop our previous

            sum_so_far = nums[i] + sum_so_far

            if sum_so_far > maximum_sum_so_far:
                maximum_sum_so_far = sum_so_far
                right_pointer = i

            if sum_so_far < 0:
                left_pointer = left_pointer + 1
                sum_so_far = 0 # penalize that pick

        return 0


if __name__ == '__main__':
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]

    # changed = sorted(nums)

    print(Solution.largestSubarraySum(Solution, nums))
