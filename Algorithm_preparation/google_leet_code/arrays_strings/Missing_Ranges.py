from typing import List


class Solution:

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        missingRanges = []

        for  index,elem in enumerate(nums):
            if elem >= lower and elem < upper:

                if( elem - lower)> 1 :
                    if elem-1 == lower+1:
                        missingRanges.append(str(lower+1))
                    else:
                        missingRanges.append(str(lower+1) + "->" + str(elem- 1))
                lower = elem

        if lower < upper:
            missingRanges.append(str(lower + 1) + "->" + str(upper))

        return missingRanges


if __name__ == '__main__':
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(Solution.findMissingRanges(Solution,nums,lower,upper))
    #Output: ["2","4->49","51->74","76->99"]



