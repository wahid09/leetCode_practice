class Solution:
    def braces(self, A):
        stack=[]
        ops = ['+','*', '/', '-']
        for i in A:
            if i == '(':
                stack.append(i)
            if i in ops and stack:
                stack.pop()

        if not stack:
            return 0
        else:
            return 1

if __name__ == '__main__':
    s = Solution()
    result = s.braces("(a + (a + b))")
    print(result)
