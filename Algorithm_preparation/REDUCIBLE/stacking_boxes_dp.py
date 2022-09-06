class Box:
    __length = 0  # double underscore for private identifier
    __width = 0
    __height = 0
    name = ""

    def __init__(self, length: int, width: int, height: int,name:str):
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


class BoxStacking:

    def sort_boxes(boxes: list) -> list:

        sorted_by_length = sorted(boxes, key=lambda x: x.get_length(), reverse=False)

        print("Boxes sorted by the lenght are as follows :- ")
        # print(sorted_by_length)
        for _ in sorted_by_length:
            _.print_properties()

        return sorted_by_length  # in increasing  order

    def can_be_stacked(first: Box, second: Box) -> bool:
        if first.get_width() < second.get_width() and  first.get_length() < second.get_length() :
            return True

        return False

    def stack_boxes(self, boxes: list):

        sorted_by_legth_boxes = self.sort_boxes(boxes)

        heights_when_boxes_with_bases = {Box : Box.get_height() for Box in sorted_by_legth_boxes}

        for i in range(1,len(sorted_by_legth_boxes)):

            current_box = sorted_by_legth_boxes[i]

            #collect the boxes that can be stacked on top of the chosen current_box
            S = [ sorted_by_legth_boxes[j] for j in range(i) if self.can_be_stacked(sorted_by_legth_boxes[j],current_box)]

            heights_when_boxes_with_bases[current_box] = current_box.get_height() + max( [heights_when_boxes_with_bases[current_box] for Box in S],default=0)

        return max(heights_when_boxes_with_bases.values(),default=0)



if __name__ == '__main__':
    input_boxes = [[1, 5, 4], [1, 2, 2], [2, 3, 2], [2, 4, 1], [3, 6, 2], [4, 5, 3]]

    box1 = Box(1, 5, 4,"box1")
    box2 = Box(1, 2, 2,"box2")
    box3 = Box(2, 3, 2,"box3")
    box4 = Box(2, 4, 1,"box4")
    box5 = Box(3, 6, 2,"box5")
    box6 = Box(4, 5, 3,"box6")

    box_collection = [box1, box2, box3, box4, box5, box6]

    print(BoxStacking.stack_boxes(BoxStacking, box_collection))
