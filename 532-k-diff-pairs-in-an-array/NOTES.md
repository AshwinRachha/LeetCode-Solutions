# 1, 1, 3, 4, 5 k = 2
# 1, 2, 3, 4, 5 k = 1
# 0, 1, 2, 2, 3, 3, 3,
nums.sort()
start, end = 0, 1
seen = set()
while start< len(nums) and end < len(nums):
if end!=start and nums[end] - nums[start] == k:
seen.add((nums[start], nums[end]))
end+=1
elif nums[end] - nums[start] < k:
end += 1
else:
start+=1
return len(seen)