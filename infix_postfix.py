def get_precedence(char) -> int:
    match char:
        case '~':
            return 5
        case '=':
            return 4
        case '>':
            return 3
        case '&':
            return 2
        case '|':
            return 1
        case _:
            return -1


def infix_to_postfix(infix_exp):
    result = []
    stack = []

    for i in range(len(infix_exp)):
        char = infix_exp[i]

        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while stack and (get_precedence(char) < get_precedence(stack[-1]) or (
                    get_precedence(char) == get_precedence(stack[-1]))):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    print(''.join(result))
