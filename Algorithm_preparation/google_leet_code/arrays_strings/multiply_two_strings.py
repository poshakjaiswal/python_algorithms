from collections import deque


# for index, char_value in enumerate(s):
#     #print(str(index) + char_value)
#     for i in range ( last_pointer,len(s)):
#         pass


from typing import List


class Solution:


    def multiply(self, num1: str, num2: str) -> str:



        #output= []

        last_carry = 0

        solution = [ ]

        zero_counter = 0
        num = 0

        for char1 in reversed(num1):

            current = int(char1)
            output = []

            for char2 in reversed(num2):

                mult = ( int(char2) * current )+ last_carry
                currentcarry = mult // 10
                last_carry = currentcarry
                output.append(mult % 10)

            output.append(last_carry)
            output.reverse()


            temp  = zero_counter

            while temp :
                output.append(0)
                temp = temp -1

            solution.append(output)
            last_carry = 0 #initialize back

            zero_counter = zero_counter +1

            num =  num + int(''.join(map(str, output)))



        return  str(num)




if __name__ == '__main__':
    # x = "2"
    # y = "3"
    #
    #
    # print(Solution.multiply(Solution, x,y))

    x = "123"
    y = "456"

    print(Solution.multiply(Solution, x, y))








