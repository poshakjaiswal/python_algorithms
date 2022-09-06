from typing import List

class Solution:

    def longestIncreasingSequenceRecursive(self,inputNumbers: List[int] )-> int:

        return 0


    # Using Dynamic programming to find the lenght of longest subsequence
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


if __name__ == '__main__':

    arr = [3,1,8,2,5]
    arr1 = [5,2,8,6,3,6,9,5]

    print( Solution.longestIncreasingSequence(Solution,arr1))

