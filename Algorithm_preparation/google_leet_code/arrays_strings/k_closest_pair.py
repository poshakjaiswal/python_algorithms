import math

from typing import  List

from collections import OrderedDict,Counter



class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        output = []

        outputDict  = OrderedDict()


        for point in points:

            eucledian_distance = (point[0] * point[0] + point[1] * point[1]  )

            # output.append(eucledian_distance )

            if eucledian_distance in outputDict:

                outputDict[eucledian_distance].append(point)
            else:
                outputDict[eucledian_distance] = [point]

        temp = []

        for key in outputDict.keys():
            temp.append(key)

        x = sorted(temp)

        for i in range(k):
            output.append(outputDict[x[i]] )


        return output



if __name__ == '__main__' :
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2

    points = [[1, 3], [-2, 2]]
    k = 1
    print(Solution.kClosest(Solution,points,k))






