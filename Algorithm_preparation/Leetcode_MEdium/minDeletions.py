#https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


from collections import  *
class Solution:

    def minDeletions(self, s: str) -> int:
        frequency = dict()
        seenCharacters = set()
        frequencyArray = []

        for char in s:
            if char not in seenCharacters:
                frequency[char] = 1
                seenCharacters.add(char)
            else:
                frequency[char] = frequency[char] + 1

        for item in frequency:
            frequencyArray.append(frequency[item])

        # sort the array
        sortedFrequencies1 = sorted(frequencyArray, reverse=True
                                    )

        left_pointer = 0
        right_pointer = 1
        seen_frequency = set()
        while right_pointer < len(sortedFrequencies1):

            if sortedFrequencies1[left_pointer] == sortedFrequencies1[right_pointer]  and left_pointer!=right_pointer:
                sortedFrequencies1[right_pointer] = sortedFrequencies1[right_pointer] - 1
                left_pointer = left_pointer + 1
                right_pointer = right_pointer + 1
            else:



                right_pointer = right_pointer + 1
                left_pointer = left_pointer + 1



        return    sum(frequencyArray) - sum(sortedFrequencies1)





    def minDeletions1(self, s: str) -> int:
        frequency = dict()
        seenCharacters = set()
        frequencyArray = []


        for char in s:
            if char not in seenCharacters:
                frequency[char] = 1
                seenCharacters.add(char)
            else:
                frequency[char] =  frequency[char] + 1

        for item in frequency:
            frequencyArray.append(frequency[item])

        #sort the array
        sortedFrequencies1 = sorted(frequencyArray,reverse= True
                                   )

        sortedFrequencSum = sum(sortedFrequencies1)

        sortedFrequencies = sortedFrequencies1.copy()

        solution_space = set(sortedFrequencies)



        for x in solution_space:
            sortedFrequencies.remove(x)


        for i in  range(0,len(sortedFrequencies)):
            current_max = max(sortedFrequencies, default=0)

            temp = current_max

            while current_max >=0  and len(solution_space) < len(sortedFrequencies1) :
                current_max = current_max -1
                if current_max not in solution_space:

                    if current_max >=0 :
                        solution_space.add(current_max)

                    if temp in sortedFrequencies:

                        sortedFrequencies.remove(temp)


        return sortedFrequencSum - sum(solution_space)


if __name__ == '__main__':
    #s = "aab"
    # s=  "accdcdadddbaadbc"
    # s = "aaabbbcc"
    # s=  "abcabc"
    # s= "aaabbbcc"
    #
    # s= "ceabaacb"
    #
    s= "aaaabcd"
    #s= "abcabc"
    s= "aaabbbcc"

    s= "accdcdadddbaadbc"
    s= "aaabbbcc"
    s = "aab"

    s = "aab"


    s = "aaaabcd"
    s = "aaabbbcc"
    s = "accdcdadddbaadbc"
    s = "abcabc"


    print(Solution.minDeletions(Solution,s))