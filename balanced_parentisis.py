def checkBalance(s):
    # mystack = Stack(len(s))
    # if s == "":
    #     return True
    # for c in s:
    #     if c == "(" or c == "{":
    #         mystack.push(c)  # push the opening bracket
    #     else:
    #         if mystack.is_empty():
    #             return False
    #         if c == "{" and mystack.peek() != "}":  # the brackets dont match
    #             return False
    #         if c == "(" and mystack.peek() != ")":  # the brackets dont matchs
    #             return False
    #         mystack.pop()  # pop matching brackets
    #
    # if mystack.is_empty():  # stack must be empty at the end
    #     return True
    # return False
    if s is None:
        return True
    stack = []
    for t in s:
        if t == ')':
            try:
                current = stack.pop()
                if current != '(':
                    return False
            except:
                return False
        elif t == '}':
            try:
                current = stack.pop()
                if current != '{':
                    return False
            except:
                return False
        elif t == ']':
            try:
                current = stack.pop()
                if current != '[':
                    return False
            except:
                return False
        else:
            stack.append(t)
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(checkBalance("(){}"))
    print(checkBalance("()((("))
    print(checkBalance("()(}"))