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


graph_AZ1 = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"],}

graph_AZ = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"],
   "G":[],
   "H":[],
   "I":[],
   "J":[], }

from Graph_Algos import graph_search


# Test suite to chek if the graph algorithms are working correctly
class GraphTestCases(unittest.TestCase):
    def test_person_present_in_graph_bfs(self):
        graph_instance = graph_search.GraphSearch(graph)
        search_result = graph_instance.breadth_first_search("thom")
        self.assertEqual(True, search_result)

    def test_person_absent_in_graph_bfs(self):
        graph_instance = graph_search.GraphSearch(graph)
        search_result = graph_instance.breadth_first_search("poshak")
        self.assertEqual(False, search_result)

    def test_person_present_in_graph_dfs(self):
        graph_instance = graph_search.GraphSearch(graph_AZ)
        graph_instance.root_node = "A"
        search_result = graph_instance.depth_first_search("H")
        self.assertEqual(True, search_result)

# https://likegeeks.com/depth-first-search-in-python/
    def test_person_absent_in_graph_dfs(self):
        graph_instance = graph_search.GraphSearch(graph_AZ)
        graph_instance.debug_flag = True
        graph_instance.root_node = "A"
        search_result = graph_instance.depth_first_search("R")
        self.assertEqual(False, search_result)


if __name__ == '__main__':
    unittest.main()
