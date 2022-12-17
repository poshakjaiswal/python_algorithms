from collections import deque,Counter


# for index, char_value in enumerate(s):
#     #print(str(index) + char_value)
#     for i in range ( last_pointer,len(s)):
#         pass
class Solution :


    def lengthOfLongestSubstring(self,s: str) -> int:


        # def allElementsWithSingleFrequency(a:Counter)->bool:

        left = 0
        right = 0

        unique_chars = set()

        maximum = 0

        while right < len(s):

            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                right =  right + 1
                maximum = max(maximum,right- left)
            else:
                unique_chars.remove(s[left])
                left = left + 1
        return maximum


    def lengthOfLongestSubstring1( s: str) -> int:
        temp_set = set()
        left_pointer = 0
        right_pointer = 0
        current_max = 1
        final_max = 0

        for i in range ( 0,len(s)):
            target_left_character = s[left_pointer]
            target_right_character = s[right_pointer]
            if( target_left_character != target_right_character):
                temp_set = set()

                for z in range ( left_pointer , right_pointer+1):
                    temp_set.add(s[z])

                current_max = right_pointer - left_pointer + 1  # check in that window all characters are different
                if ( len(temp_set) !=  current_max) :
                    current_max = 0

            elif( (target_left_character == target_right_character ) and  left_pointer < right_pointer  ):
                left_pointer = left_pointer + 1

            right_pointer= right_pointer + 1
            final_max = max(current_max,final_max)


        return final_max





if __name__ == '__main__':
    input_string = "abcabcbb"
    print(Solution.lengthOfLongestSubstring(Solution,input_string))



