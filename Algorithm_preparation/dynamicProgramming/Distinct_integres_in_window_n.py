from typing import List

class Solution:
    def distinctElementsInGivenWindow(self, inputNumbers: List[int],window :int) -> List:
        collectionOfDistinctNumbersinWinows = []
        for i in range(0, (len(inputNumbers) - window) +1  ):
             dictionaryOfCurrentElements= set()
             for j in range( i, i + window):
                 dictionaryOfCurrentElements.add(inputNumbers[j])

             collectionOfDistinctNumbersinWinows.append(len(dictionaryOfCurrentElements))

        return collectionOfDistinctNumbersinWinows


if __name__ == '__main__':

    arr = [5, 1, 1, 3, 0]
    n = 3
    # n = 1, output = {1, 1, 1, 1, 1}
    # n = 3, output = {2, 2, 3}
    # n = 5, output = {4}

    print( Solution.distinctElementsInGivenWindow(Solution,arr,n))

