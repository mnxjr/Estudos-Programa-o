try:
    from typing import List
except:
    pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
# 46 ms

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)

#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i

#         return []  # No solution found