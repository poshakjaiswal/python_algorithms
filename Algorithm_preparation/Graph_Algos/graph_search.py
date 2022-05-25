from collections import deque


class GraphSearch:
    debug_flag = False
    graph_to_search = {}
    root_node = "you"

    def __init__(self, given_graph_to_search):
        setattr(self, 'graph_to_search', given_graph_to_search)
        pass

    @staticmethod
    def print_helper(persons_already_searched, queue_to_put_people_for_searching):
        print("----------------")
        print(" person already searched")
        print(persons_already_searched)
        print("----------------")
        print(" queue_to_put_people_for_searching")
        print(queue_to_put_people_for_searching)
        print("----------------")

        return

    def search_using_bfs(self, person_to_search="jonny"):
        search_queue = deque()
        search_queue += self.graph_to_search[self.root_node]  # you # when you are given a start position
        already_searched = []
        # key, search_queue = graph.popitem()
        while search_queue:  # if the queue is not empty
            current_person = search_queue.popleft()
            if current_person not in already_searched:
                if current_person == person_to_search:
                    return "Yes you Found " + current_person
                else:
                    search_queue += self.graph_to_search[current_person]
                    already_searched.append(current_person)

        return "No we did notfor  for  find who you were looking in your connections"

    def depth_first_search(self, person_to_search="thom"):

        persons_already_searched = []
        stack_to_put_people_for_searching = []
        stack_to_put_people_for_searching += self.graph_to_search[self.root_node]
        if self.debug_flag:
            self.print_helper(persons_already_searched, stack_to_put_people_for_searching)

        while stack_to_put_people_for_searching:  # check the queue is already not empty

            if self.debug_flag:
                self.print_helper(persons_already_searched, stack_to_put_people_for_searching)
            current_person = stack_to_put_people_for_searching.pop(-1)  # getting the last item from the queue

            if self.debug_flag:
                print("current person -->> " + current_person)

            if current_person not in persons_already_searched:

                if current_person == person_to_search:
                    return True
                else:

                    stack_to_put_people_for_searching += (self.graph_to_search[current_person])
                    persons_already_searched.append(current_person)

        return False

    def breadth_first_search(self, person_to_search="thom"):
        persons_already_searched = []
        queue_to_put_people_for_searching = []
        queue_to_put_people_for_searching += self.graph_to_search[self.root_node]
        if self.debug_flag:
            self.print_helper(persons_already_searched, queue_to_put_people_for_searching)

        while queue_to_put_people_for_searching:  # check the queue is already not empty

            if self.debug_flag:
                self.print_helper(persons_already_searched, queue_to_put_people_for_searching)
            current_person = queue_to_put_people_for_searching.pop(0)  # getting the first item from the queue

            if self.debug_flag:
                print("current person -->> " + current_person)

            if current_person not in persons_already_searched:

                if current_person == person_to_search:
                    return True
                else:
                    # See that append adds a single element to the list, which may be anything. +=[] joins the lists.
                    '''
                    >>> a=[]
                    >>> a.append([1,2])
                    >>> a
                    [[1, 2]]
                    >>> a=[]
                    >>> a+=[1,2]
                    >>> a
                    [1, 2]
                    '''
                    queue_to_put_people_for_searching += (self.graph_to_search[current_person])
                    persons_already_searched.append(current_person)

        return False
