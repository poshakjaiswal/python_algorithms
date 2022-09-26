from collections import deque


# for index, char_value in enumerate(s):
#     #print(str(index) + char_value)
#     for i in range ( last_pointer,len(s)):
#         pass


from typing import List


class Solution:


    def nextPermutation(self, nums: List[int]) -> List[int]:

        leftPointer = len(nums) - 1
        rightPointer = len(nums) - 1

        x = deque()

        left_cand = 0
        right_cand = 0



        #Find First Decreasing Number
        while leftPointer > 0    :
           if  nums[rightPointer]  > nums[leftPointer]: #swap

               left_cand = leftPointer
               break

           elif nums[leftPointer]  >= nums[rightPointer]:
               leftPointer =  leftPointer - 1

        element_at_left_candidate = nums[left_cand]

        for i in  range(left_cand, len(nums)):
            if element_at_left_candidate < nums[i]:  # swap
                nums[left_cand], nums[i] = nums[i], nums[left_cand]
                break





        if ((rightPointer - leftPointer) + 1 ) == len(nums) :#Strictly decreasing order
            nums.reverse()
        return nums

if __name__ == '__main__':
    nums = [1,2,3]
    #nums = [2, 3, 1]
    #nums = [3, 2, 1]
    #nums = [1, 1, 5]

    nums = [1,5,8,4,7,6,5,3,1]

    print(" Test " + str(nums))
    print(Solution.nextPermutation(Solution, nums))

    nums = [1, 2, 3]

    print(" Test " + str(nums))
    print(Solution.nextPermutation(Solution,nums))



    nums = [1, 3,2]
    print(" Test " + str(nums))
    print(Solution.nextPermutation(Solution, nums))

    nums = [2, 1, 3]
    print(" Test " + str(nums))
    print(Solution.nextPermutation(Solution, nums))

    nums = [2, 3, 1]
    print(" Test " + str(nums))
    print(Solution.nextPermutation(Solution, nums))



