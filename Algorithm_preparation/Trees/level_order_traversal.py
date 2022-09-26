from typing import List

from collections import deque


class TreeNode:
    __left =  None
    __right = None
    __data = None

    def __init__(self,data):
        self.__data = data

    def setLeft(self,left ):
        self.__left = left
    def setRight(self,right ):
        self.__right = right

    def getLeft(self ):
        return self.__left

    def getRight(self ):
        return self.__right

    def getData(self):
        return self.__data


class Solution:



    def traversTreeLevelOrder(self, rootNode: TreeNode) -> List[TreeNode]:

        if rootNode == None:
            return []

        queue = deque()
        output = dict()
        queue.append(rootNode)
        level = 0
        while queue:

            auxillary_space = []

            while queue:
                auxillary_space.append(queue.pop())

            output[level] = auxillary_space.copy()

            for item in  auxillary_space:
                if item.getLeft() != None:
                    queue.append(item.getLeft())
                if item.getRight() != None:
                    queue.append(item.getRight())

            level = level +1



        return output


if __name__ == '__main__':


    root_F = TreeNode("F")

    node_B = TreeNode("B")

    node_G = TreeNode("G")

    node_A = TreeNode("A")

    node_D = TreeNode("D")

    node_I = TreeNode("I")

    node_C = TreeNode("C")

    node_E = TreeNode("E")
    node_H = TreeNode("H")

    #Make connections
    root_F.setLeft(node_B)
    root_F.setRight(node_G)

    node_B.setLeft(node_A)
    node_B.setRight(node_D)


    node_G.setRight(node_I)

    node_D.setLeft(node_C)
    node_D.setRight(node_E)

    node_I.setLeft(node_H)



    print(" ------ IN Level------")
    print(Solution.traversTreeLevelOrder(Solution, root_F))





