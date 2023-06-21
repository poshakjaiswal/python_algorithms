from typing import  List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bottom_up approach of dp

        product_ending_at_index = [1] * (len(nums) + 1)

        for index, elem in enumerate(nums):

            if  (elem * product_ending_at_index[index ]) <  product_ending_at_index[index ]:
                product_ending_at_index[index + 1] = product_ending_at_index[index ]

            else :
                product_ending_at_index[index + 1] = max(product_ending_at_index[index ],
                                               elem * product_ending_at_index[index ],elem)


        return max(product_ending_at_index)


if __name__ == '__main__':
    coins = [2,3,-2,4]


    print(Solution.maxProduct(Solution,coins))

