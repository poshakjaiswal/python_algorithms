from typing import List

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


    # left root right
    def traversTreeInorder(self, rootNode: TreeNode)->TreeNode:

         if rootNode == None:
            return None

         if rootNode.getLeft() != None:
             self.traversTreeInorder(self,rootNode.getLeft())

         if rootNode != None:
            print(rootNode.getData())


         if rootNode.getRight() != None:
             self.traversTreeInorder(self, rootNode.getRight())

    def traversTreePreorder(self, rootNode: TreeNode)->TreeNode:

         if rootNode == None:
            return None

         if rootNode != None:
            print(rootNode.getData())

         if rootNode.getLeft() != None:
             self.traversTreePreorder(self,rootNode.getLeft())


         if rootNode.getRight() != None:
             self.traversTreePreorder(self, rootNode.getRight())






    def traversTreePostorder(self, rootNode: TreeNode)->TreeNode:

         if rootNode == None:
            return None

         if rootNode.getLeft() != None:
             self.traversTreePostorder(self,rootNode.getLeft())


         if rootNode.getRight() != None:
             self.traversTreePostorder(self, rootNode.getRight())

         if rootNode != None:
            print(rootNode.getData())


    def traversTreePreorderIterative(self, rootNode: TreeNode)->List[TreeNode]:

         if rootNode == None:
            return []

         stack = [ rootNode,]
         output = []

         while stack:
             current_node = stack.pop()
             if current_node is not None:
                 output.append(current_node.getData())
                 if current_node.getRight() is not None:
                     stack.append(current_node.getRight())
                 if current_node.getLeft() is not None:
                     stack.append(current_node.getLeft())


         return output

    def traversTreeInorderIterative(self, rootNode: TreeNode) -> List[TreeNode]:

        if rootNode == None:
            return []

        stack = [ ]
        output = []

        while stack or rootNode!=None:
            if rootNode != None:
                stack.append(rootNode)
                rootNode = rootNode.getLeft()

            else:
                rootNode = stack.pop()
                output.append(rootNode.getData())
                rootNode = rootNode.getRight()






        return output


    def traversTreePostorderIterative(self, rootNode: TreeNode) -> List[TreeNode]:

        if rootNode == None:
            return []

        stack = [rootNode, ]
        output = []

        while stack:
            current_node = stack.pop()
            if current_node is not None:

                if current_node.getRight() is not None:
                    stack.append(current_node.getRight())
                output.append(current_node.getData())

                if current_node.getLeft() is not None:
                    stack.append(current_node.getLeft())

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

    # print(" ------ IN ORDER------")
    # print( Solution.traversTreeInorder(Solution,root_F))
    #
    # print(" ------ IN PRE------")
    # print(Solution.traversTreePreorder(Solution, root_F))
    #
    # print(" ------ IN POST------")
    # print(Solution.traversTreePostorder(Solution, root_F))

    print(" ------ IN PRE------")
    print(Solution.traversTreePreorderIterative(Solution, root_F))

    print(" ------ IN ORDER------")
    print(Solution.traversTreeInorderIterative(Solution, root_F))




