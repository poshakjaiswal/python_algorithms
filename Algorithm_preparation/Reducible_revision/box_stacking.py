
'''
Given n boxes [(L1, W₁, H1), (L2, W2, H2), ..., (Ln, Wn, Hn)] where box i has
length Lį, width Wį, and height Hi, find the height of the tallest possible stack
Box (Li,Wi, Hi) can be on top of box (Lj, Wj, Hj) if Lį < Lj, W i; < Wj.
[(4, 5, 3), (2, 3, 2), (3, 6, 2), (1, 5, 4), (2, 4, 1), (1, 2, 2)]

'''

class Box:
    __length = 0  # double underscore for private identifier
    __width = 0
    __height = 0
    name = ""

    def __init__(self, length: int, width: int, height: int ,name :str):
        if (length <= 0 or width <= 0 or height <= 0):
            print("Non Negative Values")
        self.__length = length
        self.__width = width
        self.__height = height
        self.name = name

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def print_properties(self):
        print(self.name  )

class StackBoxes:

    def canBeStacked(self,Box1: Box , Box2 : Box)->bool:

        if ((Box1.get_length() < Box2.get_length())  and (Box1.get_width() < Box2.get_width()) ):
            return True

        return False

    def maximumStackLength(self, Boxes: list)->int:
        #sort the boxes based on their length
        #Boxes.sort()
        sorted_by_length = sorted(Boxes, key=lambda x: x.get_length(), reverse=False)

        heights = dict()
        for Box in sorted_by_length:
            box_name = Box.name
            heights[box_name] = Box.get_height()

        for Box in sorted_by_length:
            box_name = Box.name

            Box_under_evaluation = Box

            S = set() # set of boxes that can be stacked on top of my current Box
            for boxes  in sorted_by_length :
                current_box = boxes
                if self.canBeStacked(self,Box_under_evaluation,current_box):
                    S.add(current_box)
            heights[box_name] = Box_under_evaluation.get_height() + max( [heights[box_name] for Box in S] ,default=0)

        return max(heights.values(),default=0)





if __name__ == '__main__':
    input_boxes = [[1, 5, 4], [1, 2, 2], [2, 3, 2], [2, 4, 1], [3, 6, 2], [4, 5, 3]]

    box1 = Box(1, 5, 4, "box1")
    box2 = Box(1, 2, 2, "box2")
    box3 = Box(2, 3, 2, "box3")
    box4 = Box(2, 4, 1, "box4")
    box5 = Box(3, 6, 2, "box5")
    box6 = Box(4, 5, 3, "box6")

    boxes = [box1,box2,box3,box4,box5,box6]


    print( StackBoxes.maximumStackLength(StackBoxes ,boxes))
