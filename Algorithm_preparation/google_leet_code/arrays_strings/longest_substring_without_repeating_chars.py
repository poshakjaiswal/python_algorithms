from collections import deque
from typing import List


class Solution:


    def longestIncreasingSequence(self, inputNumbers: List[int] )-> int:

        #Initialize the array with 1
        lis_tracker = [1] * len(inputNumbers)

        for i in range (0 , len(inputNumbers)):

            #Subproblems that means all those elements which satisfy the condition that they are less than the current element
            subproblem = []

            #subproblems = [ lis_tracker[k] for k in range(i) if inputNumbers[k] < inputNumbers[i]]

            for j in range (0 , i):
                 if ( inputNumbers [j] < inputNumbers[i]):
                     subproblem.append(lis_tracker[j])


            #lis_tracker[i] =  1 + max(subproblems,default=0)
            lis_tracker[i] = 1 + max(subproblem, default=0)


        return max(lis_tracker,default=0)


#Time Limit Exceeded : VERY BAD :(
    def lengthOfLongestSubstring0(self,s: str) -> int:

        if len(s) == 0:
            return 0
        maximum = 1


        m,n = len(s),len(s)

        #grid = [ [ 0 for x in range(n)] for y in range(m)]
        for i in range(0,len(s)+1):
            current_window = set()
            for j in range(i,len(s)+1 ):
                sample =  s[i:j]
                print(sample)
                #current_window1 = [*sample]
                current_window1 =  list(sample)
                current_window = set(current_window1)
                if ((len(current_window) > maximum) and (len(sample) == (len(current_window)))):
                    maximum = len(current_window)



        return maximum

# Time Limit Exceeded : VERY BAD :(
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        maximum = 1

        m, n = len(s), len(s)

        grid = [ [ 0 for x in range(n)] for y in range(m)]
        for i in range(0, len(s) ):
            current_window = set()
            row_max = 1
            for j in range(i, len(s) ):

                if s[j] not in current_window:
                    grid[i][j] = 1 + grid[i][j-1]

                current_window.add(s[j])
                if grid[i][j] > row_max:
                    row_max = grid[i][j]


            maxi = row_max

            if maxi > maximum :
                maximum = maxi


        return maximum


    def lengthOfLongestSubstringLinear(self, s: str) -> int:

        if len(s) == 0:
            return 0
        maximum = 1
        m = len(s)
        PAIR = [ 0 ,0]
        current_window = set()
        grid = [1] * m
        current_window.add(s[0])
        for i in range(1, len(s) ):

            if s[i] not in current_window:
                grid[i] = 1 + grid[i-1]

            current_window.add(s[i])

        maximum = max(grid)


        return maximum



    def lengthOfLongestSubstringRED(self,s: str) -> int:
        # Base condition
        if s == "":
            return 0
        # Starting index of window
        start = 0
        # Ending index of window
        end = 0
        # Maximum length of substring without repeating characters
        maxLength = 0
        # Set to store unique characters
        unique_characters = set()
        # Loop for each character in the string
        while end < len(s):
            if s[end] not in unique_characters:
                unique_characters.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique_characters))
            else:
                unique_characters.remove(s[start])
                start += 1
        return maxLength

    

if __name__ == '__main__':
    input_string = "abcabdcbb"
    #input_string = "ABRACADABRA"
    #input_string = "bbbbb"
    #input_string = "pwwkew"
    #print(Solution.lengthOfLongestSubstring(Solution,input_string))

    print(Solution.lengthOfLongestSubstringRED(Solution, input_string))





