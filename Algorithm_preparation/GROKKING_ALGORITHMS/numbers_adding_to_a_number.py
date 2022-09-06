def bottom_up_approach_numbers_adding_up_to_a_number(arr, target_total) -> int:
    pass




def recursive_numbers_adding_up(arr: tuple, target_total: int, current_index: int) -> int:
    if target_total == 0:  # base case
        return 1

    elif target_total < 0:  # negative case
        return 0
    elif current_index >= len(arr):
        return 0

    elif target_total < arr[current_index]:
        recursive_numbers_adding_up(arr, target_total, current_index + 1)
    else:
        return recursive_numbers_adding_up(arr, target_total - arr[current_index],
                                           current_index - 1) + recursive_numbers_adding_up(arr, target_total,
                                                                                            current_index - 1)


def recursive_numbers_adding_up1(arr: tuple, target_total: int, current_index: int) -> int:
    if target_total == 0:  # base case
        return 1

    elif target_total < 0:  # negative case
        return 0
    elif current_index  >= (len(arr)-1):
        return 0

    elif target_total > arr[current_index]:
        recursive_numbers_adding_up(arr, target_total, current_index + 1)
    else:
        return recursive_numbers_adding_up(arr, target_total - arr[current_index],
                                           current_index + 1) + recursive_numbers_adding_up(arr, target_total,
                                                                                            current_index + 1)


if __name__ == '__main__':
    arr = [2, 4, 6, 10]
    target_total = 16
    # print(bottom_up_approach_numbers_adding_up_to_a_number(n))
    print(recursive_numbers_adding_up(arr, target_total, 0))
