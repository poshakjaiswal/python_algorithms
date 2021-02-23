class LongestCommonSubstring:
    first_string = ""
    second_string = ""

    def __init__(self, first_input_string, second_input_string):
        self.first_string = first_input_string
        self.second_string = second_input_string

        pass

    # private method
    def __check_which_item_to_pick(self, cost_matrix, current_row, current_col):

        print(cost_matrix)
        print("--------------")

        print("--------------")

        print("current row -- > " + str(current_row))
        print("current col -- > " + str(current_col))
        print("--------------")
        cost_matrix[current_row][current_col] += cost_matrix[current_row-1][current_col-1]

        if self.first_string[current_row] == self.second_string[current_col]:
            cost_matrix[current_row][current_col] += 1


    def __find_max_element_in_matrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        max_item = -1

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] >= max_item:
                    max_item = matrix[i][j]

        return max_item



    def check_length_of_longest_common_substring(self):

        rows, cols = len(self.first_string), len(self.second_string)

        # create a 2D matrix and initialize it with 0
        cost_matrix = [[0 for col in range(cols)] for row in range(rows)]

        # start filling the matrix
        for i in range(rows):
            for j in range(cols):
                 self.__check_which_item_to_pick(cost_matrix, i, j)

        max_common_substring = self.__find_max_element_in_matrix(cost_matrix)
        print(" Maximum Common Substring length >> " + str(max_common_substring))
        return max_common_substring
