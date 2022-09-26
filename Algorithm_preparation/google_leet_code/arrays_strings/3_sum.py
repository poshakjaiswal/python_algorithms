from collections import deque


# for index, char_value in enumerate(s):
#     #print(str(index) + char_value)
#     for i in range ( last_pointer,len(s)):
#         pass
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

       possible_sum = set()

       solution = []
       present_elems =  dict()

       dict_elem = dict()
       for i in range(0, len(nums)):
           present_elems[i] = nums[i]
           for j in range( i , len(nums)):

               if ( i != j ):
                   key = str(i) + "_" +str(j)
                   #if dictionary already contains that
                   current_sum = nums[i] + nums[j]

                   dict_elem[key] = current_sum
                   possible_sum.add(current_sum)

       disctinct_answer = set()
       for key in dict_elem:
            value = dict_elem[key]
            i_index,j_index = key.split("_")
            output_candidate = []

            i_index = int(i_index)
            j_index = int (j_index)


            flag = ""

            for k in range ( 0 , len(nums)):

                if ( k != i_index  and i != j_index and  k != j_index) :
                    if ( value +nums[k]  == 0 ):
                        print(" i->" + str(i_index )+ " j->" + str(j_index ) + " k->" + str(k ))
                        output_candidate = sorted( [nums[i_index], nums[j_index],nums[k]])
                        flag = str(output_candidate)


                if len(output_candidate) > 0 and flag not in disctinct_answer :
                    solution.append(output_candidate)
                    disctinct_answer.add(flag)

                output_candidate = []



       return sorted(solution)



#00
#01
#02
#0,3




if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]

    changed = sorted(nums)

    print(Solution.threeSum(Solution,changed))



