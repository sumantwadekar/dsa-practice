from stack_impl import Stack

def is_matching_parentheses(opening, closing):
    if (opening == '(' and closing == ')') or (opening == '(' and closing == ')') or (opening == '(' and closing == ')'):
        return True
    return False


def check_balanced_parentheses(string) -> bool:
    print(string)
    stc = Stack()
    matching_parentheses = { '}': '{', ')': '(', ']': '[' }
    for char in string:
        # print(char)
        if char in ['(', '[', '{']:
            stc.put(char)
        else:
            top = stc.pop()
            if top != matching_parentheses[char]:
                return False
    return len(stc.stack) == 0

print(check_balanced_parentheses("[][()[]()]"))
