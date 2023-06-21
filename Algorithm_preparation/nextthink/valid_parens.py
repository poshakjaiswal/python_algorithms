def remove_unbalanced_parenthesis(string):
    stack = []
    result = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                continue
        result.append(char)

    return ''.join(result)

# Example usage
string = "ab(a(c)fg)9)"
balanced_string = remove_unbalanced_parenthesis(string)
print(balanced_string)
