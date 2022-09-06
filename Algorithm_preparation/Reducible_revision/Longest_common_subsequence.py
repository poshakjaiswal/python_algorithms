from typing import List

class Solution:


    def longest_common_subsequence(self, first:str, second:str )-> int:

        #create a grid
        #Adding extra 1 so that diagonal doesn;t get into out of bounds
        m = len(first)+1
        n = len(second)+1


       # grid = [[0] * m]*n   #python shallow list issues

        grid = [ [ 0 for x in range(n)] for y in range(m)]
        max_count = 0
        for i in range( 0 , len(first)):
            for j in range(0,len(second)):
                if( first[i] == second[j]):
                    grid[i+1][j+1] = 1 + grid[i][j]
                    if ( grid[i+1][j+1] >= max_count):
                        max_count = grid[i+1][j+1]
                else:
                    grid[i+1][j+1] = max(grid[i+1][j],grid[i][j+1] )

        return max_count






if __name__ == '__main__':

    first = "FISH"
    second = "FOSH"

    first1 = "abg"
    second1 = "abcdefg"

    first2 = "AGGTAB"
    second2 = "GTXAYB"




    print( Solution.longest_common_subsequence(Solution,second,first))
    print( Solution.longest_common_subsequence(Solution,second1,first1))
    print(Solution.longest_common_subsequence(Solution, second2, first2))



