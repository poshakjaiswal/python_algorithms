

import heapq
from heapq import heapify,heappop,heappush


class solution:


    def findSmallestNumber(self,nums):

        heapify(nums)





        return nums.heappop()









if __name__ == "__main__":
    s = solution()
    nums = [15,14,1,3,5,6]
    smallest = s.findSmallestNumber(nums)

    print(smallest)
