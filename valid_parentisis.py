class Solution:
    # def isValid(self, s):
    #     for i in range(len(s)):
    #         if s[0] == s[i+1]:
    #             return True
    #         else:
    #             return False

    # workable
    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False

    def isValid(self, s):
        # sizeOfS = len(s)
        # t = [0] * len(s)
        # top = -1
        # loopUp = {")": "(", "}": "{", "]": "["}
        # if (sizeOfS % 2 != 0):
        #     return False
        # else:
        #     for i in range(0, sizeOfS):
        #         if (s[i] in ('(', '{', '[')):
        #             top += 1
        #             t[top] = s[i]
        #         else:
        #             if (t[top] == loopUp[s[i]]):
        #                 top -= 1
        #             else:
        #                 return False
        #     if (top != -1):
        #         return False
        # return True

        if s is None:
            return True
        stack = []
        for t in s:
            print(f"This value is T: {t}")
            if t == ')':
                try:
                    print(f"Stack is: {stack}")
                    current = stack.pop()
                    print(f"Current is : {current}")
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
    s = Solution()
    res = s.isValid("()[]{}")
    print(res)