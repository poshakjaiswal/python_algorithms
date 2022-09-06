from typing import List


class Solution:

    def diagonal_traversal(self,matrix: List[List[int]],row_index:int,col_index :int)-> bool: #corner index

        last_seen = matrix[row_index][col_index]

        row = row_index
        col = col_index
        for i in range (col_index,0,-1):

            if row >= 0 and col>= 0 :
                current_element = matrix[row][col]
                print("i >> " + str(row) + " j >> " + str(col) + " Value >> " + str(current_element))

                if last_seen != current_element:
                    return False
                row = row -1
                col = col -1
                last_seen = current_element



        return True
    def isTopelitzMatrix(self, matrix: List[List[int]]) -> bool:#All Diagonal elements are same


        isTopelitzMatrix = True

        total_rows = len(matrix)
        total_columns = len(matrix[0])

        # for i in range( total_rows ,0,-1):
        #     for j in range(total_columns,0,-1):
        #         print ( "i >> " + str(i)  + " j >> " + str(j) + " Value >> " + str(matrix [i-1][j-1]))


        for i in range (0,total_columns): #traverse with bottom row in mind

            print("Checking For R,C Value >> " +  str(total_rows-1)   + " " + str(i))


            isTopelitzMatrix = isTopelitzMatrix  and self.diagonal_traversal(self,matrix,total_rows-1,i)


        for j in range (0,total_rows):
            print("Checking For R,C Value >> " + str(j) + " " + str(total_columns-1) + " " )

            isTopelitzMatrix = isTopelitzMatrix  and self.diagonal_traversal(self,matrix,j,total_columns-1)


        return  isTopelitzMatrix



if __name__ == '__main__':
    #input_matrix = [[1,2,3,4], [5,1,2,3],[6,5,1,2]]

    input_matrix = [[1, 2], [2, 2]]

    print(Solution.isTopelitzMatrix(Solution,input_matrix))

    # print(Solution.diagonal_traversal(Solution, input_matrix,2,3))
    # print(Solution.diagonal_traversal(Solution, input_matrix, 2, 2))
    # print(Solution.diagonal_traversal(Solution, input_matrix, 2, 0))
    # print(Solution.diagonal_traversal(Solution, input_matrix, 0,3))
    # print(Solution.diagonal_traversal(Solution, input_matrix, 2, 1))
    # print(Solution.diagonal_traversal(Solution, input_matrix, 1, 3))
