class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        string_stack = []
        s_replaced = s.replace("-", "")
        first_break = len(s_replaced) % k
        groups = k

        if first_break > 0:
            string_stack.append(s_replaced[0:first_break])
            string_stack.append("-")

        first_pointer = first_break
        next_pointer = first_pointer + groups

        for i in range(first_break, len(s_replaced), groups):
            substring = s_replaced[i:next_pointer]
            string_stack.append(substring)
            next_pointer += groups
            string_stack.append("-")

        if len(string_stack) > 1:
            string_stack.pop()
        return ''.join(map(str, string_stack)).upper()


if __name__ == '__main__':
    # s = "5F3Z-2e-9-w"
    # k = 4

    # s = "2-5g-3-J"
    # k = 2

    # s = "2-4A0r7-4k"
    # k= 3

    s= "---"
    k = 3

    print(Solution.licenseKeyFormatting(Solution, s, k))
