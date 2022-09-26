
from typing import  List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        dimension =  len(matrix[0]) - 1

        column = 0


        for i in range(0,dimension + 1):

            row =  dimension

            for j in range ( 0 , dimension +1 ):

                print( "ij ->" +  str(i) + " " + str(j) +  "and  "+ "rc ->" + str(row) + " " + str(column))


                temp =  matrix[i][j]

                matrix[i][j] =  matrix[row][column]

                # matrix[row][column] = temp
                row = row - 1


            column = column + 1


        return matrix













if __name__ == '__main__' :
    #matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(Solution.rotate(Solution,matrix))






