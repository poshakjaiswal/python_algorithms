
from typing import  List

import platform

class stacky(List):

    stack = []

    def push(self,obj):
        self.stack.append(obj)

    def len(self):
        return len(self.stack)


    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0 :
            return self.stack[-1] # pythonic way to return the last element of the list

        return None


class Solution:

    def isValid(self, s: str) -> bool:

        print(platform.python_version())


        def removeElements(self,input : str)->bool:

            stack  = stacky()

            matching = dict()


            matching[')'] = '('
            matching['}'] = '{'
            matching[']'] = '['

            for char in input:
                last_element = stack.peek()
                if last_element and  char in matching and last_element ==  matching[char]:
                    stack.pop()
                else:
                     stack.push(char)
            return stack.len() == 0


        return removeElements(self,s)



if __name__ == '__main__' :

    #s = "()[]{}"
    # s = "(]"
    # s= "([)]"
    # s= "(){}}{"

    s= "{[]}"
    print(Solution.isValid(Solution,s))






