'''
    1. 两数之和

    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return None

    def twoSum2(self, nums, target):
        tempDict = {}
        for i in range(0, len(nums)):
            anotherNum = target-nums[i]
            if anotherNum in tempDict:
                return [tempDict[anotherNum], i]
            tempDict[nums[i]] = i
        return None


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum2([2, 7, 11, 15], 22))
print(sol.twoSum([2, 7, 11, 15], 99))
print(sol.twoSum2([2, 7, 11, 15], 199))
