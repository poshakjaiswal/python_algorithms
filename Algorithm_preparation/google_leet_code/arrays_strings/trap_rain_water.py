from collections import deque


# for index, char_value in enumerate(s):
#     #print(str(index) + char_value)
#     for i in range ( last_pointer,len(s)):
#         pass
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:

        start = 0
        end = len(height) - 1

        maximum_capacity = 0

        while start <= end:
            current_capacity = min(height[start],height[end]) *  ( end - start)

            maximum_capacity = max( current_capacity,maximum_capacity)

            if ( height[start] <= height[end] ):
                start = start + 1

            else :
                end = end - 1

        return maximum_capacity




if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7,1]
    #height = [1,  1]
    height = [8,7,6,5,4,3,2]
    print(Solution.maxArea(Solution,height))



