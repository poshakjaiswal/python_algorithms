class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._heapify_down(0)

        return item

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Test the PriorityQueue implementation
queue = PriorityQueue()
elements = [100, 40, 20, 35, 80, 91]

for element in elements:
    queue.enqueue(element)

output = []
while True:
    item = queue.dequeue()
    if item is None:
        break
    output.append(item)

print(output)