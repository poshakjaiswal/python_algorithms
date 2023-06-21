class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        left_pointer = 0
        right_pointer = 1

        currentMax = set()

        maxi = 1

        currentMax.add(s[left_pointer])

        while right_pointer < len(s):

            # iterate throuh the characters

            if s[right_pointer] not in currentMax:

                currentMax.add(s[right_pointer])

                maxi = max(maxi, len(currentMax))

            else:

                currentMax = set()  # clean the set by reinitializing it
                currentMax.add(s[right_pointer])

            right_pointer = right_pointer + 1

        return maxi


if __name__ == "__main__":

    s = Solution()

    input =  "dvdf"
    print(s.lengthOfLongestSubstring(input))


