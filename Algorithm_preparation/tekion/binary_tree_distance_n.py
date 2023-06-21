# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to print nodes at distance dist from the given node
def print_nodes_at_distance(root, source, dist):
    # Base case: if root is None, return
    if root is None:
        return

    # If the current node is at the desired distance, print its value
    if dist == 0 and root == source:
        print(root.data, end=" ")
        return

    # Recur for the left and right subtrees
    print_nodes_at_distance(root.left, source, dist - 1)
    print_nodes_at_distance(root.right, source, dist - 1)

    # If the source node is found in the left or right subtree
    # recursively print the nodes at distance dist from the root
    if dist > 0:
        if root.left and root.left == source:
            print_nodes_at_distance(root.right, source, dist - 2)
        if root.right and root.right == source:
            print_nodes_at_distance(root.left, source, dist - 2)


# Create the binary tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Define the source node and distance
source = root.left
dist = 2

# Print the nodes at distance dist from the source node
print("Nodes at distance", dist, "from", source.data, ":")
print_nodes_at_distance(root, source, dist)
