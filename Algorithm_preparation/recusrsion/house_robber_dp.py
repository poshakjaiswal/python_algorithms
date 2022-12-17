from typing import List


class Solution:

    # dynamic Programming approach
    def rob(self, nums: List[int]) -> int:
        solution = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        solution[0] = nums[0]

        solution[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            val = max((nums[i] + solution[i - 2]), solution[i - 1])
            solution[i] = val

        return solution.pop()


if __name__ == '__main__':
    #nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    print(Solution.rob(Solution, nums))
