
from typing import  List
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        def removeElements(self,input : str)->str:
            stack = []
            for char in input:

                if len(stack) > 0 and char == '#':
                    stack.pop()
                elif char != '#':
                     stack.append(char)
            return ''.join(stack)


        return removeElements(self,s) == removeElements(self,t)



if __name__ == '__main__' :
    s = "ab#c"
    t = "ad#c"

    s= "y#fo##f"
    t= "y#f#o##f"


    print(Solution.backspaceCompare(Solution,s,t))






