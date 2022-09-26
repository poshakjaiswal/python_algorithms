from typing import List

class Solution:


    def minimumEnclosedBoxes(self, boxSizes: List[int]) -> List:

        boxSortedBasedOnSize = sorted(boxSizes,reverse=False)

        countOfDistinctEnclosures = 0

        while len(boxSortedBasedOnSize) > 0:

            boxesOfInterest = set(boxSortedBasedOnSize)


            if len(boxesOfInterest) > 0:
                countOfDistinctEnclosures = countOfDistinctEnclosures + 1

            for item in boxesOfInterest:
                boxSortedBasedOnSize.remove(item)

        return countOfDistinctEnclosures

    def minimumEnclosedBoxes(self, boxSizes: List[int]) -> List:

        boxSortedBasedOnSize = sorted(boxSizes,reverse=False)

        countOfDistinctEnclosures = 0

        while len(boxSortedBasedOnSize) > 0:

            boxesOfInterest = set(boxSortedBasedOnSize)


            if len(boxesOfInterest) > 0:
                countOfDistinctEnclosures = countOfDistinctEnclosures + 1

            for item in boxesOfInterest:
                boxSortedBasedOnSize.remove(item)

        return countOfDistinctEnclosures


if __name__ == '__main__':

    arr = [1,2,2,3,7,4,2,1]




    print( Solution.minimumEnclosedBoxes(Solution,arr))

