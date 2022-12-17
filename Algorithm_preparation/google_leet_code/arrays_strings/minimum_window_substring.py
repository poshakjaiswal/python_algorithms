from typing import List
from collections import Counter,OrderedDict

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        minWindowSubstring = ""
        #By Sliding window approach

        left = 0
        right = 0

        count = Counter()
        count.update(t)

        dynamic_counter = Counter()

        min_window = len(s)

        solution = []
        def isSubset(a:Counter,b:Counter)->bool:

            x = a   -  b

            if len(x) == 0 :
                return True

            return False
        while right <= len(s):


            if(isSubset(count,dynamic_counter) ):# check if frequencies match
                solution.append([left,right]) # One possible solution
                current_min = right-left
                if current_min <= min_window :
                    minWindowSubstring = s[left:right]

                    min_window = current_min

                dynamic_counter[s[left]] = dynamic_counter[s[left]] - 1
                left = left + 1
                #Contract
            else:
                if right < len(s):
                    dynamic_counter.update(s[right])
                right = right + 1

        return minWindowSubstring


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "a"
    t = "aa"
    # s = "a"
    # t = "a"
    print(Solution.minWindow(Solution,s,t))




