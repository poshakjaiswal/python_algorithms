from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minlen = 201

        count = 0

        for elem in strs:
            minlen = min(minlen, len(elem))

        collector = []

        for elem in strs:
            collector.append(list(elem))

        for r in range(0, minlen):

            flag = True

            prev = collector[0][r]
            for c in range(0, len(collector)):

                if prev != collector[c][r]:
                    flag = False
                    return strs[0][0:count]

            if flag:
                count = count + 1

        return strs[0][0:count]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]

    strs = ["cir", "car"]
    # strs = ["dog", "racecar", "car"]
    print(Solution.longestCommonPrefix(Solution, strs))
