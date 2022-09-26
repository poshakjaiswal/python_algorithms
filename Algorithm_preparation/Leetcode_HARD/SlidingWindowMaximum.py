from typing import List
from collections import deque
import math

class Solution:

    def maxSlidingWindow1(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:

        window_max = max( nums[0:k])
        solution = []
        solution.append(window_max)

        local_maximum_window = deque()

        local_maximum_window.append(window_max)


        if k == 1 :
            local_maximum_window.popleft()

        def clean_dequeue(current_dequeue,number_under_observation):
            if len(current_dequeue) >= k:
                number = len(current_dequeue) - k + 1

                while number:
                    current_dequeue.popleft()
                    number = number - 1

            for item in current_dequeue:
                if number_under_observation < item:
                    current_dequeue.remove(item)


        for i  in range( k, len(nums) ):

            clean_dequeue(local_maximum_window,nums[i])

            if len(local_maximum_window)  == 0:
                current_element = -math.inf
            else:
                current_element = local_maximum_window.pop()

            window_max = max(nums[i],current_element)
            solution.append(window_max)
            local_maximum_window.append(nums[i])



        return  solution

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        window_max = max( nums[0:k])
        solution = []
        solution.append(window_max)

        local_maximum_window = deque()

        local_maximum_window.append(window_max)


        for i  in range( k, len(nums) ):

            current_element = local_maximum_window.pop()
            window_max = max(nums[i],current_element)
            solution.append(window_max)
            local_maximum_window.append(window_max)

        return  solution





if __name__ == '__main__':



    nums = [1]
    k = 1



    nums0 = [1, 3, -1, -3, 5, 3, 6, 7]
    #3


    nums = [1, -1]
    k = 1

    nums3 = [7,2,4]
    k3 = 2

    nums1 = [3, 1, -1, -3, 5, 3, 6, 7]
    k1 = 3


    #print(Solution.maxSlidingWindow1(Solution,nums,k))
    print(Solution.maxSlidingWindow1(Solution, nums1, k1))
    #print(Solution.maxSlidingWindow1(Solution, nums3, k3)) # 7,4
