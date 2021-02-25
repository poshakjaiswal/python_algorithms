#Author Poshak
class Knapsack:
    knapsack = {}
    available_items_to_pick = 0
    total_capacity = 0

    def __init__(self, knapsack_passed, total_capacity):
        self.knapsack = knapsack_passed
        self.available_items_to_pick = len(self.knapsack)
        self.total_capacity = total_capacity
        pass

    # private method
    def __check_which_item_to_pick(self, cost_matrix, current_row, current_col):

        print(cost_matrix)
        print("--------------")

        print("--------------")

        print("current row -- > " + str(current_row))
        print("current col -- > " + str(current_col))
        print("--------------")

        aggregated_value = 0

        row_above_it = current_row - 1

        # 1 Take item above it
        previous_maximum = cost_matrix[row_above_it][current_col]  # the item above it ( upar waala)

        # 2

        cost_of_current_item = self.knapsack[current_row]['C']
        weight_of_current_item = self.knapsack[current_row]['W']

        if weight_of_current_item <= (current_col+1):# here current_col+1 is done because the index starts at 0
            col_balance_wt = current_col - weight_of_current_item
            value_of_remaining_space = 0
            if (current_col+1) - weight_of_current_item > 0 : # here current_col+1 is done because the index starts at 0
                value_of_remaining_space = cost_matrix[row_above_it][col_balance_wt]
            aggregated_value = value_of_remaining_space + cost_of_current_item

        cost_to_fill = max(previous_maximum, aggregated_value)

        return cost_to_fill

    def find_items_to_pick(self):

        print(self.knapsack)
        print(" Total Capacity  >> " + str(self.total_capacity))
        print(" Available Items to pick  >> " + str(self.available_items_to_pick))
        rows, cols = self.available_items_to_pick, self.total_capacity

        # create a 2D matrix and initialize it with 0

        # cost_matrix = [[0] * cols] * rows
        cost_matrix = [[0 for col in range(cols)] for row in range(rows)]

        # start filling the matrix
        for i in range(rows):
            for j in range(cols):
                cost_matrix[i][j] = self.__check_which_item_to_pick(cost_matrix, i, j)

        print(" Maximum Weight that can be stolen >> " + str(cost_matrix[rows - 1][cols - 1]))

        print("------<<<>>>>>>Final for Longest Knapsack problem <<<<<<<>>>>>--------")
        print(cost_matrix)
        print("--------------")
        return cost_matrix[rows - 1][cols - 1]
