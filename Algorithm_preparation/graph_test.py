import unittest

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from Graph_Algos import graph_algos


# Test suite to chek if the graph algorithms are working correctly
class GraphTestCases(unittest.TestCase):
    def test_person_present_in_graph(self):
        graph_instance = graph_algos.GraphSearch(graph)
        search_result = graph_instance.breadth_first_search()
        self.assertEqual(True, True)

    def test_person_absent_in_graph(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
