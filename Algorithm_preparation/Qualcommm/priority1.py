from heapq import heapify,heappop

class PriorityQueue:

    def __init__(self):
        self.heap = []

    def insert(self, priority):
        self.heap.append(priority)
        heapify(self.heap)

    def extract_max(self):
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")

        max_value = heappop(self.heap)


        return max_value


def main():
    pq = PriorityQueue()
    pq.insert(100)
    pq.insert(40)
    pq.insert(20)
    pq.insert(35)
    pq.insert(80)
    pq.insert(91)

    out = []

    k = 3

    while  pq.heap:
        out.append(pq.extract_max())



    for index, item in reversed(list(enumerate(out))):

        if k > 0:
            print(item)
        k= k-1







if __name__ == "__main__":
    main()