from collections import defaultdict
from typing import List

class Solution:


    def totalFruit(self, fruits: List[int]) -> int:


        keys_tracker = defaultdict(int)
        max_value = 0
        left_pointer,right_pointer = 0,0

        for right_pointer in range(len(fruits)):
            keys_tracker[fruits[right_pointer]] = keys_tracker[fruits[right_pointer]]  + 1

            current_total_keys = len(keys_tracker.keys())
            if current_total_keys <=2:

                max_value = max(max_value, right_pointer - left_pointer + 1)

            elif current_total_keys > 2: #slide the pointer of left side and discard the last seen first element


                # decrease the count of the beginning integer
                keys_tracker[fruits[left_pointer]] -= 1

                # and if the count of the interger is zero, we don't need it anymore so pop it
                if keys_tracker[fruits[left_pointer]] == 0:
                    keys_tracker.pop(fruits[left_pointer])

                # shift the left pointer to the right, so we have a new starting pointer
                left_pointer += 1

        return max_value


    def totalFruit1(self, fruits: List[int]) -> int:

        top_two = []
        count =0

        for i in fruits:
            if len(top_two) < 2:
                top_two.append(i)

            if i > top_two[-1]  and i != top_two[0]:
                top_two[1] = i

            if len(top_two) == 2:
                if top_two[0] < top_two[1] :
                    top_two[0],top_two[1] = top_two[1],top_two[0] #swap

        for j in fruits:
            if (j == top_two[0] or j == top_two[1]):
                count = count+1

        return count

    def totalFruitFrequency(self, fruits: List[int]) -> int:

        freqMap = {}

        for i in range(len(fruits)):
            if (fruits[i] in freqMap):
                # If number is present in freqMap,
                # incrementing it's count by 1
                freqMap[fruits[i]] = freqMap[fruits[i]] + 1
            else:
                # If integer is not present in freqMap,
                # putting this integer to freqMap with 1 as it's value
                freqMap[fruits[i]] = 1

        print(freqMap)

        return 0



if __name__ == '__main__':

    #fruits = [1, 2, 1]
    #fruits = [1, 2, 3, 2, 2]
    #fruits = [0,1,2,2]
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

    print(Solution.totalFruit(Solution,fruits))
