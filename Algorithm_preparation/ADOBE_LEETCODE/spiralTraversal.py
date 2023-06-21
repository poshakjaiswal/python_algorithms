from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        visited = set()

        output = []

        def getKey(r_current, c_current):

            if r_current < len(matrix) and c_current < len(matrix[0]) and r_current >= 0  and c_current>=0:
                return str(str(r_current) + "_" + str(c_current))

            else:
                return None

        def getDirection(r_current, c_current,last):
            if getKey(r_current, c_current):

                dir = last

                if getKey(r_current, c_current + 1) and getKey(r_current,
                                                               c_current + 1) not in visited:  # if right is not visited
                    dir = "right"

                elif getKey(r_current + 1, c_current) and getKey(r_current + 1, c_current) not in visited:
                    dir = "down"

                elif getKey(r_current, c_current - 1) and getKey(r_current, c_current - 1) not in visited:
                    dir = "left"
                elif getKey(r_current - 1, c_current) and getKey(r_current - 1, c_current) not in visited:

                    dir = "up"

                if dir == "right":
                    return [r_current, c_current + 1]
                elif dir == "down":
                    return [r_current + 1, c_current]

                elif dir == "left":
                    return [r_current, c_current - 1]

                elif dir == "up":
                    return [r_current - 1, c_current]


        next_cord = [0, 0]
        last = "right"

        while len(visited) < len(matrix) * len(matrix[0]):
            output.append(matrix[next_cord[0]][next_cord[1]])

            key = getKey(next_cord[0], next_cord[1])

            visited.add(key)
            [next_cord,last ] = getDirection(next_cord[0], next_cord[1],last)

        return output


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    print(Solution.spiralOrder(Solution, matrix))
