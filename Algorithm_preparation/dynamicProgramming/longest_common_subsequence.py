""""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
 A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
  For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

  https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
"""


class LongestCommonSubsequence:
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
        diagonal_left = cost_matrix[current_row - 1][current_col - 1]

        if self.first_string[current_row] == self.second_string[current_col]:
            cost_matrix[current_row][current_col] = diagonal_left + 1
        else:
            item_on_top = cost_matrix[current_row-1][current_col]
            item_previous_in_same_row = cost_matrix[current_row][current_col-1]
            cost_matrix[current_row][current_col] = max(item_on_top,item_previous_in_same_row)
            pass

    def check_length_of_longest_common_substring(self):

        rows, cols = len(self.first_string), len(self.second_string)

        # create a 2D matrix and initialize it with 0
        cost_matrix = [[0 for col in range(cols)] for row in range(rows)]

        # start filling the matrix
        for i in range(rows):
            for j in range(cols):
                self.__check_which_item_to_pick(cost_matrix, i, j)

        max_common_subsequence = cost_matrix[rows-1][cols-1]
        print(" Maximum Common Subsequence length >> " + str(max_common_subsequence))

        print("------<<<>>>>>>Final for Longest common Subsequence <<<<<<<>>>>>--------")
        print(cost_matrix)
        print("--------------")
        return max_common_subsequence
