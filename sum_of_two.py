# Example
# 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]

def sum_two(nums : list[int], target: int ) -> list[int]:
    array = nums
    map = {}
    for index, value in enumerate(array):
        print(index, value)
        print(map)
        diff = target - value
        if diff in map:
            return [index, map[diff]]
        map[value] = index
    return

var = sum_two([1,7,2,5],9)
print(var)