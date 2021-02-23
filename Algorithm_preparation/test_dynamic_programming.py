import unittest

from dynamicProgramming import knapsack,longest_common_substring
knapsack_items = {
       0: { #guitar
           "W": 1,
           "C": 1500
       },
       1: { #stero
           "W": 4,
           "C": 3000
       },
       2: { #laptop
           "W": 3,
           "C": 2000
       },
}

TOTAL_CAPACITY = 4


class MyTestCase(unittest.TestCase):
    def test_knapsack(self):
        initialized_knapsack = knapsack.Knapsack(knapsack_items, TOTAL_CAPACITY)
        value_returned = initialized_knapsack.find_items_to_pick()
        self.assertEqual(3500, value_returned)

    def test_longest_common_substring(self):
        first_word = "fish"
        second_word = "hish"
        initialized_lcs = longest_common_substring.LongestCommonSubstring(first_word, second_word)
        value_returned = initialized_lcs.check_length_of_longest_common_substring()
        self.assertEqual(3, value_returned)

    def test_longest_common_substring_large(self):
        first_word = "GeeksQuiz"
        second_word = "GeeksforGeeks"
        initialized_lcs = longest_common_substring.LongestCommonSubstring(first_word, second_word)
        value_returned = initialized_lcs.check_length_of_longest_common_substring()
        self.assertEqual(5, value_returned)

    def test_longest_common_substring_large(self):
        first_word = "GeeksforGeeks"
        second_word = "GeeksQuiz"
        initialized_lcs = longest_common_substring.LongestCommonSubstring(first_word, second_word)
        value_returned = initialized_lcs.check_length_of_longest_common_substring()
        self.assertEqual(5, value_returned)


if __name__ == '__main__':
    unittest.main()
