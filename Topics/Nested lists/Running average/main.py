nums = [int(_) for _ in input()]
print([(nums[_] + nums[_ + 1]) / 2 for _ in range(len(nums) - 1)])