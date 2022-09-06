graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque


class Solution:
    def breadth_first_search(self, graph_passed, person_to_search="") -> bool:
        persons_looked_so_far = deque()

        persons_looked_so_far.append("you")  # assume that we start from you as the initial position
        visited = {}

        while len(persons_looked_so_far) > 0:
            evaluate_person = persons_looked_so_far.popleft()
            if evaluate_person == person_to_search:
                return True
            elif evaluate_person not in visited:
                persons_looked_so_far += graph[evaluate_person]
            visited[evaluate_person] = True

        return False


if __name__ == '__main__':
    print(Solution.breadth_first_search(Solution, graph, "jonny"))
