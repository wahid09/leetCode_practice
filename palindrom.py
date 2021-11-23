class Solution:
    def isPalindrome(self, x):
        temp = x
        sum = 0
        r = 0
        while x > 0:
            r = x % 10
            sum = sum * 10 + r
            x = x // 10
        if sum == temp:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    re = s.isPalindrome(121)
    print(re)
