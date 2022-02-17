for i in range(index, len(nums)):
if i > index and nums[i] == nums[i-1]:
continue
if nums[i] > target: break
path.append(nums[i])
backtrack(i+1, nums, ans, path, target - nums[i])
path.pop()