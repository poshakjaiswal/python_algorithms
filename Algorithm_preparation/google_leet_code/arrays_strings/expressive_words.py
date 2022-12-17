from typing import  List

from collections import OrderedDict,Counter

class Solution:

    def expressiveWords(self, s: str, words: List[str]) -> int:

        referenceWord = Counter()
        referenceWord.update(list(s))

        solution = 0


        for query in words:
            coun = Counter()
            coun.update(list(query))
            count = 0

            if referenceWord.keys() == coun.keys():

                for elem in coun:
                    if  (referenceWord[elem]  ==   coun[ elem])  or   (referenceWord[elem]   >= 3 ):
                        count = count + 1
                if count == len(coun):
                    solution = solution +1


        return solution



if __name__ == '__main__' :

    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(Solution.expressiveWords(Solution,s,words))






