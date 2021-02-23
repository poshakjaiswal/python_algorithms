import unittest

from dynamicProgramming import knapsack
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
    def test_something(self):
        initialized_knapsack = knapsack.Knapsack(knapsack_items, TOTAL_CAPACITY)
        value_returned = initialized_knapsack.find_items_to_pick()
        self.assertEqual(3500, value_returned)


if __name__ == '__main__':
    unittest.main()
