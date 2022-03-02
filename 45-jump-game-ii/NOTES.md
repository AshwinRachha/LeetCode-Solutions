jumps = 0
max_index = 0
currentJumpEnd = 0
for i in range(len(nums)-1):
max_index = max(max_index, nums[i] + i)
if i == currentJumpEnd:
jumps+=1
currentJumpEnd = max_index
return jumps