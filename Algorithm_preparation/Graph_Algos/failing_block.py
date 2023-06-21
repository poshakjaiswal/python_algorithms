def apply_gravity(block):
    rows = len(block)
    cols = len(block[0])

    for row in range(rows - 2, -1, -1):
        for col in range(cols):
            if block[row][col] != 0:
                current_row = row
                while current_row < rows - 1 and block[current_row + 1][col] == 0:
                    block[current_row + 1][col] = block[current_row][col]
                    block[current_row][col] = 0
                    current_row += 1

    return block


def find_failing_element(block):
    block = apply_gravity(block)

    rows = len(block)
    cols = len(block[0])

    for row in range(rows):
        for col in range(cols):
            if block[row][col] != 0:
                if row == rows - 1 or (row < rows - 1 and block[row + 1][col] != 0):
                    return row, col

    return None


# Example usage
block = [[0, 1, 0, 1],
         [1, 0, 0, 1],
         [0, 0, 1, 0],
         [0, 1, 0, 0]]

failing_element = find_failing_element(block)
if failing_element is not None:
    print("Failing element coordinates:", failing_element)
else:
    print("No failing element found.")
