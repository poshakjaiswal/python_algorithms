from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        out = []

        window = 0

        for el in words:
            window = window + len(el)

        words = sorted(words,reverse=True)

        wordsize = len(words[0][0])

        for i in range(0, len(s) - window+1):

            subpart = s[i:i+window]

            count = 0

            for elem in words:

                index = subpart.find(elem)

                if index >= 0:
                    subpart =  subpart.replace(elem,"",1)
                    count = count + 1
                else :
                    break

            if count == len(words) :
                out.append(i)


        return out



if __name__ == "__main__":
    # s = "barfoofoobarthefoobarman"
    # words = ["bar","foo","the"]

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]

    s= "ababaab"
    words = ["ab", "ba", "ba"]
    print(Solution.findSubstring(Solution, s,words))