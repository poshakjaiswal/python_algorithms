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

        cost_to_fill = 0
        value_of_current_item = self.knapsack[current_row].C
        value_of_remaining_space = cost_matrix[current_row - 1][current_col - self.knapsack[current_row].W]

        previous_maximum = cost_matrix[current_row - 1][current_col]  # the item above it ( upar waala)

        cost_to_fill = max(previous_maximum, value_of_remaining_space)

        return cost_to_fill

    def find_items_to_pick(self):

        print(self.knapsack)
        print(" Total Capacity  >> " + str(self.total_capacity))
        print(" Available Items to pick  >> " + str(self.available_items_to_pick))
        rows, cols = self.available_items_to_pick, self.total_capacity

        # create a 2D matrix and initialize it with 0
        cols += 1
        rows += 1
        cost_matrix = [[0] * cols] * rows
        # cost_matrix = [[0 for i in range(cols)] for j in range(rows)]
        print(cost_matrix)

        # start filling the matrix
        for i in range(cols):
            for j in range(rows):
                cost_matrix[i][j] = self.__check_which_item_to_pick(cost_matrix, i, j)

        print(" Maximum Weight that can be stolen >> " + str(cost_matrix[rows][cols]))
