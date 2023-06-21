#binary tree


"""

Print all nodes at distance `dist` from a given node. No parent pointers are available.

         20
       /    \
      8     22
    /  \
   4   12
      /  \
    10   14

Input:
root - Root of binary tree
source - Node from which distance need to be calculated
dist - distance

source = Node(8)
dist = 2.

Output : 10 14 22

source = Node(14)
dist = 3.

Output : 4 20


///
"""
   #level order traversal

# 20                -> 0
#
# 8 , 22             -> 1
#
# 4 ,12              -> 2
#
# 10 , 14            ->3
#
#
# x, y        -->  4

class Node:
    val = 0
    left = None
    right = None

    __init__:




def findNDistanceElements(root,source,distance):

    output =  []

    def awayFromRoot(root, distance):

        if root is None or source is None:
            return 0

        if distance == 0:
            return root

        else:
            distance = distance - 1
            elementsAtDistance(root.left, source, distance)
            elementsAtDistance(root.right, source, distance)



    def elementsAtDistance(root,source,distance):

        if root is None or source is None :
            return 0

        elif  source == root:

            return distance

        else:
            distance = distance  + 1
            elementsAtDistance(root.left,source,distance)
            elementsAtDistance(root.right, source, distance)


    distanceOfSourceFromRoot = elementsAtDistance(root,source,0)    #8 ,  #10 14 22


    #iteratre through all the nodes , (  distance of that node from root )  , target

    newCalculatedDistance = distance - distanceOfSourceFromRoot

    awayFromRoot(root,newCalculatedDistance) #22

    awayFromRoot(source, distance)





print(findNDistanceElements())
