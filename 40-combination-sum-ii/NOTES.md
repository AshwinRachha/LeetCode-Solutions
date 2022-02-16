seen = set()
candidates.sort()
def backtrack(index, nums, ans, path, target):
if target == 0:
ans.append(path[:])
return
for i in range(index, len(nums)):
if i > index and nums[i] == nums[i-1]:
continue
if nums[i] > target: break
path.append(nums[i])
backtrack(i+1, nums, ans, path, target - nums[i])
path.pop()
ans = []
backtrack(0, candidates, ans, [], target)
return ans