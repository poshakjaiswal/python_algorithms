from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #depth first search

        def createGraph( times,n_total_nodes):

            graph = {}

            #intitialize nodes in graph

            for i in range(n_total_nodes):
                graph[i] = []

            for item in times:
                graph[item[0]] =  graph[item[0]].append( item[1])


            print(graph)

        createGraph(times,n)



if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    Solution.networkDelayTime(Solution,times,n,k)
