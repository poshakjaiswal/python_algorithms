from typing import  List
class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        output = []
        current_sum = 1
        carry = 0

        for i in  reversed(digits):
            current_sum = current_sum + i + carry
            number = current_sum % 10
            carry = current_sum // 10
            output.append(number)
            current_sum = 0

        if carry > 0 :
            output.append(carry)
        output.reverse()
        return output



if __name__ == '__main__' :



    digits = [4,3,2,1]

    digits = [9]
    print(Solution.plusOne(Solution,digits))






