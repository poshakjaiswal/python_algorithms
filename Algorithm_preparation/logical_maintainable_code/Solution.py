

class Solution:

    def getFirstNonRepeatedChar(self,input:str)->str:
        if len(input) == 0 :
            return None

        seenCharacters = set()
        for char in input:
            if char not in seenCharacters:
                seenCharacters.add(char)

            else:
                seenCharacters.remove(char)

        return  list(seenCharacters)[0]

    def getFirstNonRepeatedCharWithFrequency(self, input: str) -> str:
        if len(input) == 0:
            return None

        frequency = dict()
        nonRepeatedCharacter = None
        seenCharacters = set()

        for char in input:
            if char not in seenCharacters:
                seenCharacters.add(char)
                frequency[char] = 1
            else:
                frequency[char] = frequency[char] + 1

        for elem in frequency:
            if frequency[elem] == 1:
                return elem
        return nonRepeatedCharacter





if __name__ == '__main__':

    input = "abcdeab"
    #input = "aaac"

    print(Solution.getFirstNonRepeatedCharWithFrequency(Solution,input))
