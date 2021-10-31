class Solution:
    def twoSum(self, nums, target):
        nums_set = set(nums)
        nums_len = len(nums)
        for i, x in enumerate(nums):
            if (target - x) in nums_set:
                for j in range(i+1, nums_len):
                    if (target - x) == nums[j]:
                        return [i, j]

    def tow_sum(self, nums, target):
        complement_map = dict()
        ## nums = [2, 7, 11, 15, 3, 17]
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num  # 7
            if num in complement_map:
                return [complement_map[num], i]
            else:
                complement_map[complement] = i  ## {18:0, 13:1, 9:2, 5:3, }
                print(complement_map)

    def brute_force_tow_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    re = s.tow_sum([2, 7, 11, 15, 3, 17], 20)
    print(re)
