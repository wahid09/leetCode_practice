class Solution:
    def romanToInt(self, s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        end_point = 1001
        for i in s:
            if dict[i] > end_point:
                sum = sum + dict[i] - (end_point * 2)
            else:
                sum = sum + dict[i]
            end_point = dict[i]
            if sum < 0:
                sum = -sum
        return sum

if __name__ == '__main__':
    s = Solution()
    result = s.romanToInt('IV')
    ## print(result)