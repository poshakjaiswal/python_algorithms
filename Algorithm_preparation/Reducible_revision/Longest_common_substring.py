from typing import List

class Solution:


    def longest_common_substringy(self, first:str, second:str )-> int:

        #create a grid
        #Adding extra 1 so that diagonal doesn;t get into out of bounds
        m = len(first)+1
        n = len(second)+1


       # grid = [[0] * m]*n   #python shallow list issues

        grid = [ [ 0 for x in range(m)] for y in range(n)]
        max_count = 0
        for i in range( 0 , len(first)):
            for j in range(0,len(second)):
                if( first[i] == second[j]):
                    grid[i][j] = 1 + grid[i-1][j-1]
                    if ( grid[i][j] >= max_count):
                        max_count = grid[i][j]


        return max_count






if __name__ == '__main__':

    first = "FISH"
    second = "FOSH"

    str1 = "ABCXYZAY"
    str2 = "XYZABCB"

    print( Solution.longest_common_substringy(Solution,first,second))
    print(Solution.longest_common_substringy(Solution, str1, str2))

